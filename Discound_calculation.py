
for i in range(1, 6):
    name = input("Enter name: ")
    amount = int(input("Enter amount: "))

    if amount > 5000:
        discount = 1000
    elif amount > 2000:
        discount = 500
    else:
        discount = 0

    final = amount - discount

    print("Customer:", name)
    print("Purchase Amount:", amount)
    print("Discount:", discount)
    print("Final Amount:", final)
    print("----------------")
