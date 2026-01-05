'''question 24: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers.
                If the user enters anything other than an integer, detect their mistake using try and except and print an error message and skip to the next integers.'''

num = []

while True:
    line = (input("Enter a number: "))
    if line == 'done':
        break
    try:
        num.append(int(line))
    except:
        print('invaid input')
 
print(num)
total = 0
for i in num:
    total = total + i


count = 0 
for i in num:
    count = count + 1

avg = total / count

print(total, count, avg)

'''Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the 
               average.'''

def min(num):
    smallest = None
    for i in num :
        if smallest is None or i < smallest:
            smallest = i
    return smallest

print("smallest number: " ,min(num))

def max(num):
    largest = None
    for i in num :
        if largest is None or i > largest :
            largest = i
    return largest

print("largest number: " ,max(num))