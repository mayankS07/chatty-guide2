day = int(input())
food = int(input())
flight = int(input())
hotel = int(input())
total_flight = flight * 2
total_food = food * day
total_hotel = hotel * (day - 1)
print(total_hotel + total_food + total_flight)
