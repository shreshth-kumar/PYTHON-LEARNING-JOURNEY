#head() tail()
#head() 5
#tail() 5

import pandas as pd
df = pd.read_json("Pandas\sample_Data.json")

print('Display 10 rows of first')
print(df.head())

print('Display 10 rows of last')
print(df.tail())
