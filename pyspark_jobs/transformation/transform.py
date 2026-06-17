from pyspark_jobs.extraction.extract import cust,geo,orddetails,orders,payment,prod,prodName,seller
from pyspark.sql.functions import when,col,trim,lower,expr,round
from pyspark.sql.types import StringType
from pyspark_jobs.db_connection.py_db import read_table
import uuid

def replace_na(df):
    df=df.select(
        *[
            (
                when(
                    (trim(lower(col(f.name)))=='nan') |
                    (trim(lower(col(f.name)))=='na') |
                    (trim(col(f.name))==''),
                    None
                ).otherwise(col(f.name)).alias(f.name)
                if isinstance(f.dataType,StringType)
                else col(f.name)
            )
            for f in df.schema.fields
        ]
    )
    
    return df

# Customer transformation
def cust_trans(cust):
    # Replace string NA's
    cust=replace_na(cust)
    
    # Standarize text
    cust=cust.select(
        *[
            trim(lower(col(f.name))).alias(f.name)
            if isinstance(f.dataType, StringType)
            else col(f.name)
            
            for f in cust.schema.fields
        ]
    )
    
    # Handle null value
    cust=cust.withColumn(
        'cust_unq_id',
        when(col('cust_unq_id').isNull(),expr("uuid()"))
        .otherwise(col('cust_unq_id'))
    )
    
    # Drop full empty row
    cust=cust.dropna(how='all')
    
    # Fix datatypes
    cust=cust.withColumn(
        'cust_zipcode',
        trim(col('cust_zipcode').cast('string'))
    )

    # Drop duplicated value
    cust=cust.dropDuplicates()
    cust=cust.dropDuplicates(['cust_unq_id'])
    cust=cust.dropDuplicates(['cust_id'])
    
    return cust

# Location transformation
def geo_trans(geo):
    geo=replace_na(geo)
    
    # Standarize Text
    geo=geo.select(
    *[
            (
                trim(lower(col(f.name))).cast('string').alias(f.name)
                if f.name != 'timestampp'
                else col(f.name)
            )
            for f in geo.schema.fields
        ]
    )
    
    # Standarize value
    geo=geo.withColumns({
        'geo_lat':round(col('geo_lat'),4),
        'geo_lng':round(col('geo_lng'),4)
    })
    
    # Drop duplicated value
    geo=geo.dropDuplicates()
    geo=geo.dropDuplicates(['geo_zipcode','geo_lat','geo_lng'])
    
    return geo

# Orddetails transformation
def orddetail_trans(orddetails):
    orddetails=replace_na(orddetails)
    
    # Standarize Text
    orddetails=orddetails.select(
    *[
        (
            trim(lower(col(f.name))).alias(f.name)
            if isinstance(f.dataType,StringType)
            else col(f.name)
        )
        for f in orddetails.schema.fields
    ])
    
    # Join Operation
    ord_df=read_table('silver.orders')
    ord_df=ord_df.select('order_id','order_sk')
    prod_df=read_table('silver.prod')
    prod_df=prod.select('prod_id','prod_sk')
    seller_df=read_table('silver.seller')
    seller_df=seller.select('seller_id','seller_sk')

    orddetails=(
        orddetails.alias('o')
        .join(
            ord_df.alias('ord'),
            col('o.order_id')==col('ord.order_id'),
            'left'
        )
        .join(
            prod_df.alias('p'),
            col('o.prod_id')==col('p.prod_id'),
            'left'
        )
        .join(
            seller_df.alias('s'),
            col('o.seller_id')==col('s.seller_id'),
            'left'
        )
        .select(
            'o.*',
            'ord.order_sk',
            'p.prod_sk',
            's.seller_sk'
        )
    )
    
    return orddetails
    
# Orders transformation
def ord_trans(orders):
    orders=replace_na(orders)
    
    # Handle null
    orders=orders.withColumn(
        "approved_at",
        when(
            col('approved_at').isNull(),
            expr('purchase_timestamp + INTERVAL 15 MINUTES')
        ).otherwise(col('approved_at')).alias('approved_at')
    )
    
    orders=orders.withColumn(
        'delivered_carrier_date',
        when(
            col('delivered_carrier_date').isNull(),
            expr('approved_at + INTERVAL 2 DAYS')
        ).otherwise(col('delivered_carrier_date')).alias('delivered_carrier_date')
    )
    
    orders=orders.withColumn(
        'delivered_customer_date',
        when(
            col('delivered_customer_date').isNull(),
            expr('delivered_carrier_date + INTERVAL 4 DAYS')
        )
    )
    
    # Business rule implementation
    orders=orders.withColumn(
        'delivered_carrier_date',
        when(
            col('approved_at')>col('delivered_carrier_date'),
            expr('approved_at + INTERVAL 2 DAYS')
        ).otherwise(col('delivered_carrier_date')).alias('delivered_carrier_date')
    )

    orders=orders.withColumn(
        'delivered_customer_date',
        when(
            col('delivered_carrier_date')>col('delivered_customer_date'),
            expr('delivered_carrier_date + INTERVAL 2 DAYS')
        ).otherwise(col('delivered_customer_date')).alias('delivered_customer_date')
    )

    # Handle wrong status value availability
    orders=orders.withColumn(
        'delivered_customer_date',
        when(
            col('ord_status')=='shipped',
            None
        ).otherwise(col('delivered_customer_date')).alias('delivered_customer_date')
    )   
    
    orders=orders.withColumns({
        'delivered_customer_date':when(
            col('ord_status')=='canceled',
            None
        ).otherwise(col('delivered_customer_date')),
        'estimated_delivery_date':when(
            col('ord_status')=='canceled',
            None
        ).otherwise(col('estimated_delivery_date'))
    })
    
    orders=orders.withColumns({
        'delivered_customer_date':when(
            col('ord_status')=='invoiced',
            None
        ).otherwise(col('delivered_customer_date')),
        'estimated_delivery_date':when(
            col('ord_status')=='invoiced',
            None
        ).otherwise(col('estimated_delivery_date')),
        'delivered_carrier_date':when(
            col('ord_status')=='invoiced',
            None
        ).otherwise(col('delivered_carrier_date'))
    })
    
    # Drop duplicates
    orders=orders.dropna(subset=['order_id']).dropDuplicates(['order_id'])
    
    # Cust_sk mapping
    orders=(
        orders.alias('o').join(
            cust.alias('c'),
            col('o.cust_id')==col('c.cust_id'),
            'left'
        ).select(
            'o.*',
            'c.cust_sk'
        )
    )
    
    return orders

# Payment transformation
def payment_trans(payment):
    payment=replace_na(payment)
    
    # Handling null values
    payment=payment.withColumn(
        'payment_type',
        when(
            col('payment_type').isNull(),
            'voucher'
        ).otherwise(col('payment_type')).alias('payment_type')
    )
    
    # For order_sk mapping
    payment=(
        payment.alias('p').join(
            orders.alias('o'),
            col('p.order_id')==col('o.order_id'),
            'left'
        ).select(
            'p.*',
            'o.order_sk'
        )
    )

    payment=payment.dropna(subset=['order_id']).dropDuplicates(['order_id'])
    
    return payment
    
# Product transformation
def prod_trans(prod):
    prod=replace_na(prod)
    
    prod=prod.dropDuplicates(['prod_id'])
    
    return prod
    
# Product Name transformation
def prodName_trans(prodName):
    prodName=replace_na(prodName)
    
    return prodName

# Review Transformation
def review_trans(review):
    review=replace_na(review)
    
    review=(
        review.alias('r').join(
            orders.alias('o'),
            col('r.order_id')==col('o.order_id'),
            'left'
        ).select(
            'r.*',
            'o.order_sk'
        )
    )
    
    review=review.dropDuplicates(['review_id'])
    
    return review
    
# Seller Transformation
def seller_trans(seller):
    seller=replace_na(seller)
    
    seller=seller.dropDuplicates(['seller_id'])
    

