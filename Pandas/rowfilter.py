import pandas as pd 

data ={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employees with salary > 50000')
print(high_salary)

#filtering rows salary > 50k & age > 30
filtered = df[(df['Age'] > 30) & (df['Salary'] > 50000)]
print(f'Employee list Age >30 + Salary > 50000')
print(filtered)

#using OR condition
filtered_or = df[(df['Age'] > 35) | (df['Performance_Score'] > 90)]
print('Employees older than 35 OR performance score > 90')
print(filtered_or)