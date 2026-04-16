# least common multiple 
# using eculiden algorithm 
def hcf(smallNum,largeNum):
    while(smallNum):
        numberStore = smallNum
        smallNum = largeNum % smallNum
        largeNum = numberStore

    return largeNum

# enter 2 numbers
largeNum = int(input("Enter the first number: "))
smallNum = int(input("Enter the second number: "))

# LCM is the smallest number that is two or more numbers can divide into evenly
lcm = int((smallNum / hcf(smallNum, largeNum)) * largeNum)
print("LCM is : ", lcm)