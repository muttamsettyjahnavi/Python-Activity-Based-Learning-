product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
cost = int(input("Enter cost per item: "))
selling = int(input("Enter selling price per item: "))

total_cost = quantity * cost
total_sales = quantity * selling

profit = total_sales - total_cost

print("Product Name:", product)
print("Total Cost:", total_cost)
print("Total Sales:", total_sales)
print("Profit:", profit)

if profit > 0:
    print("Business is in Profit")
elif profit < 0:
    print("Business is in Loss")
else:
    print("No Profit No Loss")
