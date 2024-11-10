marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))
marks[3] = 72.45
print(marks)

#List slicing

print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3 : -1])

#List methods

print(marks.append(4))
print(marks.sort())
print(marks.sort(reverse=True))
print(marks.reverse())
print(marks.insert(2, 90))