#"key" : value
#dictionary is mutable

info = { 
    "name" : "shreshth ",
    "learning" : "python",
    "age" : 19,
    "is adult" : True,
    "marks" : 72.40,
    "topics" : ("dictionary", "sets")
}

print(info)
print(type(info)) 
print(info["name"])
print(info["topics"])
print(info["age"])
print(info["learning"])
# print(info["surname"]) this will give error as thier is no key named surname
info["surname"] = "kumar"
print(info["surname"])

student = {
    "name" : "shreshth kumar",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

#nested dictionary

print(student["subjects"]["chem"])
print(student.keys())
print(list(student.keys()))
print(len(student)) # or print(len(list(student.keys)))
print(student.values())
print(list(student.values()))
print(student.items())
print(list(student.items()))
print(student.get("name"))
student.update({"city" : "varanasi"})
print(student)