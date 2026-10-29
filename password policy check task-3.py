password = input("Enter a password: ")

has_upper = False
has_lower = False
has_number = False

for letter in password:
    if letter.isupper():
        has_upper = True
    if letter.islower():
        has_lower = True
    if letter.isdigit():
        has_number = True

if len(password) >= 8 and has_upper and has_lower and has_number:
    print("Password is accepted")
else:
    print("Password is not accepted")
    print("It needs 8 characters, an uppercase letter, a lowercase letter, and a number.")