#read first line of file
file = open("L50/test 2.txt", "r")
print("=== Reading first line ===")
print(file.readline())
file.close()

print()

#read first 2 lines of file 
file = open("L50/test 2.txt", "r")
print("=== Reading 2 lines ===")
print(file.readline())
print(file.readline())
file.close()

print()

#looping through all the lines of the file
file = open("L50/test 2.txt", "r")
print("=== Looping through the lines ===")

for line in file:
    print(line)

file.close()