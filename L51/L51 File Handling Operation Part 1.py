# write in file using with() function
with open('L51/test.txt', 'w') as file:
    file.write("Hi I am Rahma and I am from Bangladesh.")
file.close()

# split file into words
with open('L51/test.txt', 'r') as file:
    data = file.readlines()

    print("Words in this file are:")

    for line in data:
        word = line.split()
        print (word)

file.close()