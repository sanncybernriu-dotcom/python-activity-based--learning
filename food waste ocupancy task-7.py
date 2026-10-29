number_of_days = int(input("Enter number of days: "))
maximum_waste = float(input("Enter maximum waste percentage: "))

for day in range(1, number_of_days + 1):
    prepared = int(input("Meals prepared on day " + str(day) + ": "))
    served = int(input("Meals served on day " + str(day) + ": "))

    leftover = prepared - served
    waste_percent = leftover / prepared * 100

    print("Leftover meals:", leftover)
    print("Waste percentage:", round(waste_percent, 2), "%")

    if waste_percent > maximum_waste:
        print("Waste is too high")