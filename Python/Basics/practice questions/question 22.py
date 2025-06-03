# write a recursive function to calculate the sum of first n natural numbers. 

def sum(n):
    if (n == 0):
        return 0 
    print(n)
    return sum(n-1) + n


print(sum(5))