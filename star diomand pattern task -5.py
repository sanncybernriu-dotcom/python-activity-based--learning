height = int(input("Enter the height of the diamond: "))
# Print the top half
for row in range(1, height + 1):
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)
# Print the bottom half
for row in range(height - 1, 0, -1):
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)
