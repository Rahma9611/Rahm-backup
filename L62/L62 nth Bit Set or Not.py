def setOrNot(number, n):
    mask = 1 # assuming you want to check if the bit is set or not
     
    if (n & mask) == 1 or (n & mask) == 0: # corrected comparison and OR operator
        if number & (1 << (n-1)):
            print("SET")
        else:
            print("NOT SET")

numb = int(input("Enter your number: "))   
pos = int(input("Enter the bit position to be checked: "))

setOrNot(numb, pos)