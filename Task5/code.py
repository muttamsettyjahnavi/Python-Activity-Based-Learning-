name = input("Enter customer name: ")
data = int(input("Enter data usage in GB: "))

if data <= 2:
    plan = "Basic Plan"
    bill = 199
elif data <= 5:
    plan = "Standard Plan"
    bill = 399
else:
    plan = "Premium Plan"
    bill = 599

print("Customer Name:", name)
print("Selected Plan:", plan)
print("Total Bill: Rs.", bill)
