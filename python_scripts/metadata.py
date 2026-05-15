import pandas as pd

def ingestion(df,source,batch_id):
    # Adding metadata 
    df['timestamp']=pd.Timestamp.now()
    df['source']=source
    df['batch_id']=batch_id
    
    return df
