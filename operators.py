# Define variables
a = 10
b = 5


# 1. Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

# 2. Relational Operators
print("\nRelational Operators:")
print("a == b:", a == b)  # Equal
print("a != b:", a != b)  # Not Equal
print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater than or equal to
print("a <= b:", a <= b)  # Less than or equal to

# 3. Assignment Operators
print("\nAssignment Operators:")
a += b
print("a += b:", a)
a -= b
print("a -= b:", a)
a *= b
print("a *= b:", a)
a /= b
print("a /= b:", a)
a %= b
print("a %= b:", a)
a **= b
print("a **= b:", a)
a //= b
print("a //= b:", a)

# 4. Logical Operators
print("\nLogical Operators:")
print("a > b and a < 20:", a > b and a < 20)  # Logical AND
print("a > b or a < 5:", a > b or a < 5)      # Logical OR
print("not(a > b):", not(a > b))              # Logical NOT

# 5. Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)  # Bitwise AND
print("a | b:", a | b)  # Bitwise OR
print("a ^ b:", a ^ b)  # Bitwise XOR
print("~a:", ~a)        # Bitwise NOT
print("a << 2:", a << 2)  # Left shift
print("a >> 2:", a >> 2)  # Right shift

# 6. Identity Operators
print("\nIdentity Operators:")
print("a is b:", a is b)      # Identity (is)
print("a is not b:", a is not b)  # Identity (is not)

# Example collection
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\nMembership Operators:")

print("5 in c:", 5 in c)         # Check if 5 is in the list c
print("10 not in c:", 10 not in c)  # Check if 10 is not in the list c
