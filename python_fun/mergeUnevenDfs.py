import pandas as pd 

df1 = {"col1": [1,2,3,4,5,6,7,8], "col2": ["a","b","c","d","e","f","g","h"], "col3": [1,2,3,4,5,6,7,8], "col4": ["a","b","c","d","e","f","g","h"]}

df2 = {"col5": [1,2,3], "col6": ["x","y","z"]}

def make_df(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(df)

df1 = make_df(df1)
df2 = make_df(df2)

df = pd.concat([df1,df2], axis=1)

df['col5'].fillna(df['col6'])

for i,j in zip(df['col5'].to_list(), df['col6'].to_list()):
    df['col5'].fillna(i, inplace=True)
    df['col6'].fillna(j, inplace=True)

print(df)