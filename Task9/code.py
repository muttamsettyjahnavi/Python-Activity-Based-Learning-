name = input("Enter traveler name: ")
rupees = float(input("Enter budget in Indian Rupees: "))

print("1. US Dollar")
print("2. Euro")
print("3. British Pound")

choice = int(input("Select currency: "))

if choice == 1:
    converted = rupees / 85
    print("US Dollars:", converted)
elif choice == 2:
    converted = rupees / 95
    print("Euros:", converted)
elif choice == 3:
    converted = rupees / 110
    print("British Pounds:", converted)
else:
    print("Invalid Choice")

print("Traveler Name:", name)
