import pandas as pd 

data = {
    "Time": [1,2,3,4,5],
    "Value": [10, None, 30, None ,50]
}

df = pd.DataFrame(data)
print('Before interpolation')
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print('After interpolation')
print(df)