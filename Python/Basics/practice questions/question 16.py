# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one. use subjects name as key and marks as valule.

marks = {

}

entry1 = int(input("enter your phy marks :"))
entry2 = int(input("enter your maths marks :"))
entry3 = int(input("enter your chem marks :"))

marks.update({"phy" : entry1})
marks.update({"maths" : entry2})
marks.update({"chem" : entry3})

print(marks)