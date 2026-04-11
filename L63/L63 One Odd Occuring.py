def OddOccuring(arr):
    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []
n = int(input("Enter array size: "))

while(n):
    num = int(input("Enter number of your array element:"))
    arr.append(num)
    n -= 1

print(f" OddOccurring element is: {OddOccuring(arr)}")