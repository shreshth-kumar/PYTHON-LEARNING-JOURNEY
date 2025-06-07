# pd.merge(df1, df2, on= "Column_Name", how = "type of join")

import pandas as pd 

#customer dataframe
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Ramesh','Suresh','kalpesh']
})

#order dataframe

df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

#merge
#inner join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="inner")
print('inner join')
print(df_merged)
#outer join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="outer")
print('outer join')
print(df_merged)
#left join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="left")
print('left join')
print(df_merged)
#right join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print('right join')
print(df_merged)
#cross join
df_merged = pd.merge(df_customers, df_orders, on="CustomerID", how="cross")
print('cross join')
print(df_merged)