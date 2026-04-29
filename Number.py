# 1. Using format function
def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print("Formatted result:", result)
print("Representation: Octal")

print("\n----------------------\n")

# 2. Area of circular pond and water calculation
radius = 84
pi = 3.14

area = pi * radius * radius
water = int(area * 1.4)   # no decimal

print("Area of pond:", area)
print("Total water (liters):", water)

print("\n----------------------\n")

# 3. Speed calculation
distance = 490        # meters
time = 7 * 60         # convert minutes to seconds

speed = distance // time   # no decimal

print("Speed (m/s):", speed)