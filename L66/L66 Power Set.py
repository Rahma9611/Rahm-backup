import math 
def printPowerSet(set, setSize):
    PowerSetSize = (int) (math.pow(2, setSize)) # find total elements possible in the power set
    outer = 0
    inner = 0


    for outer in range(0, PowerSetSize):
        for inner in range(0, setSize):
            # check if the inner bit in the oyter is set If set then print inner element from set 
            if ((outer & (1 << inner)) > 0):
                print(set[inner], end = "")

        print()


size = int(input("Enter array size: "))

set = []
for i in range(0,size):
    n = int(input("Enter element of the array:"))
    set.append(n)

print()

printPowerSet(set, len(set))