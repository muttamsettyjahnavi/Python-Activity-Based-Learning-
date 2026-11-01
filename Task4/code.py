name = input("Enter employee name: ")
salary = int(input("Enter basic salary: "))

hra = salary * 0.20
da = salary * 0.10
deduction = salary * 0.05

total_salary = salary + hra + da
net_salary = total_salary - deduction

print("Employee Name:", name)
print("HRA:", hra)
print("DA:", da)
print("Deduction:", deduction)
print("Net Salary: Rs.", net_salary)
