event = input("Enter event name: ")
students = int(input("Enter number of students: "))
fee = int(input("Enter registration fee per student: "))
expenses = int(input("Enter total event expenses: "))

income = students * fee
balance = income - expenses

print("Event Name:", event)
print("Total Income:", income)
print("Total Expenses:", expenses)
print("Remaining Balance:", balance)

if balance > 0:
    print("Event is in Profit")
elif balance < 0:
    print("Event is in Loss")
else:
    print("Budget is Balanced")
