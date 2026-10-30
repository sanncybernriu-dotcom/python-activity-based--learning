text = input("Enter text: ")
compressed = ""
count = 1
for i in range(len(text)):
    if i == len(text) - 1:
        compressed = compressed + text[i] + str(count)
    elif text[i] == text[i + 1]:
        count = count + 1
    else:
        compressed = compressed + text[i] + str(count)
        count = 1
print("Compressed text:", compressed)
