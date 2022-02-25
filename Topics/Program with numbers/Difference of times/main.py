hour_1 = int(input())
min_1 = int(input())
sec_1 = int(input())
hour_2 = int(input())
min_2 = int(input())
sec_2 = int(input())
hour = hour_2 - hour_1
minute = min_2 - min_1
second = sec_2 - sec_1
total_h = 3600 * hour
t_m = 60 * minute
print(total_h + t_m + second)
