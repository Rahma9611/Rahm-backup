# find the longest consecutive 1's in binary representation of a number
def max1(n):
    count = 0
    
    # count the number of iterations to reach number = 0.
    while (n != 0):
        n = (n & (n << 1)) 
        count=count+1

    return count

numb = int(input("Enter a number: "))
print(f"Longest consecutive 1's lenght : {max1(numb)}")