name = input("Enter customer name: ")
amount = int(input("Enter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.15
elif amount >= 1000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Customer Name:", name)
print("Original Amount:", amount)
print("Discount:", discount)
print("Final Bill: Rs.", final_amount)
