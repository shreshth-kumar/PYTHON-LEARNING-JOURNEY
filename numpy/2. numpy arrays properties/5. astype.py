import numpy as np

arr = np.array([1.2, 2.5, 3.8])
print(arr.dtype)
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)