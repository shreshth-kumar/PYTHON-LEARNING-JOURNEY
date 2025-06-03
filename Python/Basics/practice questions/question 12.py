#WAP to check if a lost contains a palindrome of elements. 

list1 = [1, 2, 3]
# you can edit lists one to check the code
copy_list1 = list1.copy
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")