x, y, z = input("Expression: ").split()

x = float(x)
z = float(z)
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/" and z!=0:
    result = x / z

print(f"{result:.1f}")
