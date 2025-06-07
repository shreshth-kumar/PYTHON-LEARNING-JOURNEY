"""
vertically (row-wise)
horizontallt (column-wise)

pd.concate([df1, df2], axis=0, ignore_index=True)

[df1, df2] = 
axis = 0/1

ignore_index = True
"""

#vertically
import pandas as pd 

#region1
df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Gopal','Raju']
})

#region2
df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Shyam','Baburao']
})

#concatenate vertically
df_concat = pd.concat([df_Region1, df_Region2], ignore_index=True, )
print(df_concat)

#concatenate horizontally
df_concat = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True, )
print(df_concat)