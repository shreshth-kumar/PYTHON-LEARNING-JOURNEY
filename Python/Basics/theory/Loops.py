count = 1
while count <= 5 :
    print("hello world")
    count += 1

#print numbers from 1 to 100.
i = 1 
while i <= 100 :
    print(i)
    i += 1

# print numbers from 100 to 1. 
i = 100 
while i >=1 : 
    print (i)
    i -= 1

#print the multiplication table of a number n.

n = int(input("your number :"))
i = 1 
while i <= 10 : 
    print(n* i)
    i += 1

#print the elemnents of the following list using loop : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

#search for a number x in this tuple using loops: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 36

idx = 0
while idx < len(nums):
    if(nums[idx] == x ):
        print("found at idx :", idx)
    else:
        print("finding...")
    idx += 1


#break keyword
i = 1 
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1

#FOR loops

nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)

tup = {1, 2, 3, 4, 2, 8, 9}

for num in tup:
    print(num)

str = "shreshth kumar"

for chr in str :
    print (chr)
else:
    print("END")

#  (USING FOR) print the elemnents of the following list using loop : [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in nums :
    print(val)

#  (USING FOR ) search for a number x in this tuple using loops: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = 36

idx = 0
for val in nums:
    if val == x:
        print("Number found at index", idx)
    idx += 1

# Range()

seq = range(10) # range(stop)

for i in seq:
    print(i)

for i in range(2, 10): #range(start, stop)
    print(i)

for i in range(2, 10, 2): #range(start, stop, step)
    print(i)