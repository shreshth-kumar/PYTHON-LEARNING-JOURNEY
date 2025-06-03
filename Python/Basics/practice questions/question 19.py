# WAF to print the elements of a list in a single line. (list is the parameters)

cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_elements(list):
    for item in list:
        print(item, end= " ")

print_elements(heroes)
print_elements(cities)