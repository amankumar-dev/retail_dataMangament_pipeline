from pyspark_jobs.extraction.extract import cust
from pyspark.sql.functions import when,col,trim,lower
from pyspark.sql.types import StringType

# Customer transformation
def cust_trans(cust):
    cust=cust.select(
        *[
            (
                when(
                    (trim(lower(col(f.name)))=='nan')|
                    (trim(lower(col(f.name)))=='na')|
                    (trim(col(f.name))==''),
                    None
                ).otherwise(f.name).alias(f.name)
                if isinstance(f.dataType,StringType)
                else col(f.name)
            )
            for f in cust.schema.fields
        ]
    )
    
cust_trans(cust)