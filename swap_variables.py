a = 1
b = 2
print(f"before swap: {a}, {b}")
# classical way through third variable
c = a
a = b
b = c
print(f"after first swap: {a}, {b}")

# using python syntax
a,b = b,a
print(f"after second swap: {a}, {b}")

