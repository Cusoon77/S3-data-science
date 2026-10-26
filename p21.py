import pandas as pd

data = {
    'cname':['company A','company B','company C','company D'],
    'profit':[10000,-5000,0,25000]
}

df = pd.DataFrame(data)

df['profit'] = df['profit']>0
print(df)