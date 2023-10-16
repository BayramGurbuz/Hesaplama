from math import factorial

def permutation(n, r):
    return factorial(n) // factorial(n - r)

def combination(a, b):
    return factorial(a) // (factorial(b) * factorial(a - b))

f = int(input("Enter the first number: "))

t = int(input("Enter the second number: "))

print(f"{f} elemanının {t} elemanlı permütasyonu: {permutation(f,t)}")

print(f"{f} elemanının {t} elemanlı permütasyonu: {combination(f,t)}")
