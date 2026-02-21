import random, string

print("Welcome to password generator!")

#input the lenght of passowrd
lenght = int(input("Enter the lenght of passoword:"))

#define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#combine the data
all = lower + upper + num + symbols

#use random
temp = random.sample(all, lenght)

#create the passoword
password = "".join(temp)

#print the password
print("Your random password is: "+password)