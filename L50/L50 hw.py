#open file and read its contents
file = open("L50/test 2.txt", "r")
print(file.read())
print()

file.close()

#open file and read its beginning 8 chracters
file = open("L50/test 2.txt", "r")

print("Read in parts")
print(file.read(8))
file.close()

print()

#append your name and age in the file
file = open("L50/test 2.txt", "a")
file.write("\nHi! I am Rahma and I am from Bangladesh. ")
file.close()