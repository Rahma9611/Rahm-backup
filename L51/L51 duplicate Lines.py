# program to eliminate repeated lines from a file

# creating the output file
outputFile = open('L51/test3.txt', "w")

# reading the input file
inputFile= open('L51/test2.txt', "r")

# holds lines already seen 
lines_seen_so_far = set()
print("=== Eliminatingduplicate lines ===")

for line in inputFile:
    if line not in lines_seen_so_far: # checking if line unique
        outputFile.write(line) # write unique lines in output file
        lines_seen_so_far.add(line) # adds unique lines to lines_seen_so_far

# closing the file
inputFile.close()
outputFile.close()