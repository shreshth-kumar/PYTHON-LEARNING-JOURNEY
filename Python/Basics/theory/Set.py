collection =  {1, 2, 3, 4, "hello", "world", "world"}

print(collection)
print(type(collection))
print(len(collection)) #total number of items

set = set() #empty set

print(type(set))

print(set)
set.add(1)
set.add(2)
set.add(2)

print(set)

set.remove(1)
print(set)

random = {"hello", "python", "coding", "world"}
print(random.pop())
print(random.pop())

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) #{1,2,3,4,5}
print(set1)
print(set2)