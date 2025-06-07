#sorting data
# SORTING DATA 1 COLUMN sort_values()
# df.sort_values(by="Column Name", Ture/Flase, inplace = True)

import pandas as pd

data = {
    "Name":['Arun', 'Varun', 'karan'],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
}

df= pd.DataFrame(data)
df.sort_values(by = "Age" ,ascending= False, inplace = True)
print('Sorted Age by descending')
print(df)