initial_atoms = int(input())
resulting_quantity = int(input())
a = 0
while initial_atoms >= resulting_quantity:
    half = initial_atoms // 2
    initial_atoms = half
    a += 1
x = a * 12
print(x)
