name = input("Enter patient name: ")
days = int(input("Enter number of days: "))
room = input("Enter room type (General/Private): ")

if room == "General":
    charge = 1000
elif room == "Private":
    charge = 2500
else:
    charge = 0

bill = days * charge

if bill >= 50000:
    category = "High Cost"
elif bill >= 20000:
    category = "Medium Cost"
else:
    category = "Low Cost"

print("Patient Name:", name)
print("Total Bill: Rs.", bill)
print("Patient Category:", category)
