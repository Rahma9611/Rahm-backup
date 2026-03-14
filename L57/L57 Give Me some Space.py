#calculate space complexity of the recursive function
def sum(n):
    return n*(n+1)//2

def arraysum(a): #Space complexity = 0(1), Auxiliary space = 0(1)
    sum = 0
    for i in a:
        sum = sum + i
    return sum

def sumn(n): #Space complexity = 0(n), Auxiliary space = 0(n)
    if n <= 0:
        result = 0
    else: 
        result = n + sumn(n-1)

    return result

x = 5
print(f"the sum of the first {x} number is = {sum(x)}")
print()

myArray = [4,7,12,23]
print(f"the sum of the array elements  is = {arraysum(myArray)}")
print()

y = sumn(x)
print(f"the sum of the first {x} number using recursive is = {y}")