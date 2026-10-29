classes_held = int(input("Enter classes held: "))
classes_attended = int(input("Enter classes attended: "))
required_percent = float(input("Enter required attendance percentage: "))

extra_classes = 0

while (classes_attended + extra_classes) / (classes_held + extra_classes) * 100 < required_percent:
    extra_classes = extra_classes + 1

print("You must attend", extra_classes, "more classes.")