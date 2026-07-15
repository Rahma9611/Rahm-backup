#create a new file 
new_file=open("L51/crochet.txt", "x")
new_file.close()

#check if a file exists
import os
print("=== Checking if crochet exists or not ===")

if os.path.exists("L51/crochet.txt"):
    os.remove("L51/crochet.txt")
    #print("file crochet.txt exists.")
else:
    print("The file does not exist")

    #create a new if it does not exist
    my_file = open("L51/crochet.txt", "w")
    my_file.write("I like to crochet plushies.")
    my_file.close()

#delete the folder 'L100' if it exist
if os.path.exists("L51/L100"):
    os.rmdir("L51/L100")
else:
    print("The folder does not exsist.")