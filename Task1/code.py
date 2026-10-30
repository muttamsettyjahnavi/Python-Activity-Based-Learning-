name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

if marks >= 90:
    print("Student Name:", name)
    print("Scholarship: 100%")
elif marks >= 80:
    print("Student Name:", name)
    print("Scholarship: 75%")
elif marks >= 70:
    print("Student Name:", name)
    print("Scholarship: 50%")
elif marks >= 60:
    print("Student Name:", name)
    print("Scholarship: 25%")
else:
    print("Not Eligible for Scholarship")
