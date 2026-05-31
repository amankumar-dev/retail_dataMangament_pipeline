import pandas as pd

df1=pd.DataFrame({
    'id':[1,3,1,2,4],
    'sk':['a','b',None,'c','d']
})

df2=pd.DataFrame({
    'sk':[]
})

df=df1.merge(
    df2,
    on='id',
    how='right'
)

print(df)