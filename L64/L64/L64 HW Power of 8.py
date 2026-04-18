def powerOf8(n):
    bitPosition = 0
    mask = 1

    while (bitPosition <= 63):
        mask <<= bitPosition

        # if only set bit in n
        # is at position i
        if (mask == n):
            return True
        
        bitPosition += 3
        mask = 1

    return False

numb = int(input("Enter a number: "))

if (powerOf8(numb)):
    print(f"{numb} is a power of 8.")
else:
    print(f"No {numb} is not a power of 8")