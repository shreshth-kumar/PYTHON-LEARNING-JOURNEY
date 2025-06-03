f = open("c:/Users/rkkal/Python-learning-journey/Python/Basics/theory/file input, output/demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("c:/Users/rkkal/Python-learning-journey/Python/Basics/theory/file input, output/demo.txt", "w")

f.write("I want to learn java script tomorrow. 123")

f.close()

f = open("c:/Users/rkkal/Python-learning-journey/Python/Basics/theory/file input, output/demo.txt", "a")

f.write("\nThen i will move reactJS")

f.close()

f= open("sample.txt", "a")
f.close()