import pandas as pd 

data ={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

#display the dataframe
print("Sample Dataframe")
print(df)
print("Names (single column return series)")
name = df['Name']
print(name)

# selecting multiple columns
subset = df[["Name", "Salary"]]
print('\nSubset with Name and Salary')
print(subset)