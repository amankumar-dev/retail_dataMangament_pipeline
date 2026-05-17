import pandas as pd

def ingestion(df,source,batch_id):
    # Adding metadata 
    df = df.astype(object)
    df = df.where(pd.notnull(df), None)
    df['timestampp']=pd.Timestamp.now()
    df['source']=source
    df['batch_id']=batch_id
    
    return df
