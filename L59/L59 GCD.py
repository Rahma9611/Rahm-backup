#HFC (Highest Common Factor)
largeNum = int(input("Enter the largest number: "))
smallNum = int(input("Enter the smallest number: "))

while smallNum:
    numberStore = smallNum
    smallNum = largeNum % smallNum
    largeNum = numberStore

print(f"The HFC is: ", largeNum)