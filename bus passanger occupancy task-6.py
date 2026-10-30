capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter passengers at the start: "))
number_of_stops = int(input("Enter number of stops: "))
for stop in range(1, number_of_stops + 1):
    boarding = int(input("Passengers boarding at stop " + str(stop) + ": "))
    leaving = int(input("Passengers leaving at stop " + str(stop) + ": "))
    passengers = passengers - leaving + boarding
    print("Passengers on bus:", passengers)
    if passengers > capacity:
        print("Bus capacity exceeded!")
