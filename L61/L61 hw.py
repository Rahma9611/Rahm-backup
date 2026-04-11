# implement circut

a=1
b=0
c=0

# computing all bitwise operations
aAndb = a & b
bXORc = b ^ c
bORc = b | c
g = bXORc & bORc

# calculating the final result
final = aAndb ^ g

print(f"aAndb ^ bXORc & bORc = {final}")