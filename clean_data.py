import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())
print(df.isnull().sum())

dr = df.dropna()
print(dr)
dr.to_csv("cleandata.csv",index=False)