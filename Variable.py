# 1. Value of pi and its data type
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

print("\n----------------------\n")

# 2. Using 'for' as a variable name (will cause error)
# Uncomment below line to see the error
# for = 4

print("Cannot use 'for' as a variable name because it is a reserved keyword in Python.")

print("\n----------------------\n")

# 3. Simple Interest Calculation
P = 1000   # Principal amount
R = 5      # Rate of interest
T = 3      # Time in years

SI = (P * R * T) / 100

print("Principal:", P)
print("Rate:", R)
print("Time:", T)
print("Simple Interest:", SI)