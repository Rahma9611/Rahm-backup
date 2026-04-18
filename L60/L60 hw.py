from math import sqrt

print("Two-digit prime numbers:")

# Loop through all 2-digit numbers (10 to 99)
for num in range(10, 100):
    # Prime logic: check for factors from 2 up to sqrt(num)
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i) == 0:
            break  # Found a factor, not prime
    else:
        # The 'else' belongs to the 'for' loop; 
        # it runs only if no 'break' occurred
        print(num, end=" ")