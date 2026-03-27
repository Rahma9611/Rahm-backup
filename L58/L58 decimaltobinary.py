from unicodedata import decimal


def DecimalToBinary(decimal):
    binary = ""

    while decimal > 0:
        rem = decimal % 2
        binary = str(rem) + binary
        decimal = decimal//2

    print("Binary number is:", binary)
    decimal = int(input("Enter a decimal number: "))
    
DecimalToBinary(decimal)