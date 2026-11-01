name = input("Enter passenger name: ")
age = int(input("Enter passenger age: "))
distance = int(input("Enter travel distance: "))

fare = distance * 2

if age >= 60:
    fare = fare * 0.80
elif age < 12:
    fare = fare * 0.50

print("Passenger Name:", name)
print("Travel Distance:", distance, "km")
print("Ticket Fare: Rs.", fare)

confirm = input("Confirm reservation? (yes/no): ")

if confirm == "yes":
    print("Ticket Booked Successfully")
else:
    print("Reservation Cancelled")
