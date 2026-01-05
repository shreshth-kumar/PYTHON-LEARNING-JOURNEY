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