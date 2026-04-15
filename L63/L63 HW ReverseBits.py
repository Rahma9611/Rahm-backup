def reverseBits(number):
    reversed = 0

    while (number > 0) :
        # Shift reversed number to left
        reversed = reversed << 1

        # check if last bit is 0 or 1
        # IF 1 add it using OR operation or else leave
        if (number & 1 == 1) :
            reversed = reversed ^ 1
        
        # right shift the original number
        number = number >> 1

    return reversed
numb = int(input("Enter a number: "))
print(f"Number of reversed bits: {reverseBits(numb)}")