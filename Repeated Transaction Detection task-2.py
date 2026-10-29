transaction_ids = input("Enter transaction IDs separated by spaces: ").split()
amounts = input("Enter the amounts in the same order: ").split()
limit = float(input("Enter the suspicious amount limit: "))

for i in range(len(transaction_ids)):
    # Check if this ID appeared earlier
    for j in range(i):
        if transaction_ids[i] == transaction_ids[j]:
            print("Duplicate transaction ID:", transaction_ids[i])
            break

    if float(amounts[i]) > limit:
        print("Large transaction:", transaction_ids[i], amounts[i])