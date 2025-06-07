#adding columns

import pandas as pd 

data ={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
# square brackets df["Column_Name"] = some_data

df["Bonus"] = df['Salary'] * 0.1
print(df) 

#using insert()
# df.insert(loc, "column_Name", some_data)

df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])
print(df)