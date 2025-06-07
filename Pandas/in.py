import pandas as pd

# df = pd.read_json("Pandas\sample_Data.json")

# print('displaying the info of data set')
# print(df.info())

data = {
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print('displaying the info of the data set')
print(df.info())