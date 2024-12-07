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

