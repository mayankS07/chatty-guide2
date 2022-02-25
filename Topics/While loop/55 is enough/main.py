total_number = 0
count = 0
while True:
    number = int(input())
    if number == 55:
        break
    total_number += number
    count += 1

print(count)
print(total_number)
print(round(total_number/count))
