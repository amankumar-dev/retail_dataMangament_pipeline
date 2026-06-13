from pyspark_jobs.extraction.extract import cust,geo
from pyspark.sql.functions import when,col,trim,lower,expr,round
from pyspark.sql.types import StringType
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
    ]
    
    
)