# figure out a way to store 9 and 9.0 as seprate values in the set.
# (you can take help of built-in data types)

values = {9, "9.0"} #solution 1 
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
} #solution 2 
print(values)