import pandas as pd

details_1 = {
    'cid': [1,2,3,4],
    'cname': ['a','b','c','d'],
    'stipend': [123,131,23,434],
}

details_2 = {
    'cid': [1,2,3,4],
    'cname': ['a','b','c','d'],
    'designation': ['aa','bb','cc','dd'],
}

df_1 = pd.DataFrame(details_1)
df_2 = pd.DataFrame(details_2)

dataframe = pd.merge(df_1, df_2,how = 'inner',on = 'cid')
print(dataframe)