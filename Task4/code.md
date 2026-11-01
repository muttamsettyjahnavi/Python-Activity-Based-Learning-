##  Problem Statement

The Hospital Billing and Patient Classification System is developed to calculate the hospital bill based on the number of days a patient stays in the hospital and the type of room selected.

The system takes the patient name, number of days, and room type as input. It calculates the total bill using fixed room charges.

The room charges are:
- General Room: ₹1,000 per day.
- Private Room: ₹2,500 per day.

Based on the total bill, the patient is classified into three categories:
- High Cost: ₹50,000 and above.
- Medium Cost: ₹20,000 to ₹49,999.
- Low Cost: Below ₹20,000.

Finally, the system displays the patient name, total bill, and patient category.

##  Objectives

1. To calculate hospital bills automatically.
2. To identify the room type selected by the patient.
3. To calculate charges based on the number of hospital days.
4. To classify patients based on their total bill.
5. To reduce manual calculation errors.
6. To understand Python conditional statements.

##  Assumptions

1. The patient enters a valid name.
2. The number of hospital days is entered as a whole number.
3. The room type is either General or Private.
4. General room charges are fixed at ₹1,000 per day.
5. Private room charges are fixed at ₹2,500 per day.
6. The bill is calculated by multiplying the number of days by the room charge.
7. No additional medical charges, taxes, or discounts are included.
8. The number of days must be greater than zero.

## Algorithm

Step 1: Start the program.

Step 2: Enter the patient name.

Step 3: Enter the number of hospital days.

Step 4: Enter the room type (General/Private).

Step 5: Check the room type.

- If the room is General, set the charge to ₹1,000.
- If the room is Private, set the charge to ₹2,500.
- Otherwise, set the charge to zero.

Step 6: Calculate the total bill.

Total Bill = Number of Days × Room Charge.

Step 7: Check the total bill.

- If the bill is greater than or equal to ₹50,000, category is High Cost.
- If the bill is greater than or equal to ₹20,000, category is Medium Cost.
- Otherwise, category is Low Cost.

Step 8: Display the patient name.

Step 9: Display the total bill.

Step 10: Display the patient category.

Step 11: Stop the program.

## Flowchart

```mermaid
graph TD
    A([Start]) --> B[/Enter Patient Name/]
    B --> C[/Enter Number of Days/]
    C --> D[/Enter Room Type/]
    D --> E{Room is General?}

    E -- Yes --> F[Charge = 1000]
    E -- No --> G{Room is Private?}

    G -- Yes --> H[Charge = 2500]
    G -- No --> I[Charge = 0]

    F --> J[Bill = Days * Charge]
    H --> J
    I --> J

    J --> K{Bill >= 50000?}
    K -- Yes --> L[Category = High Cost]
    K -- No --> M{Bill >= 20000?}

    M -- Yes --> N[Category = Medium Cost]
    M -- No --> O[Category = Low Cost]

    L --> P[/Display Patient Details and Bill/]
    N --> P
    O --> P

    P --> Q([Stop])
```

## Pseudocode

```text
START

INPUT patient_name
INPUT days
INPUT room

IF room = "General" THEN
    charge = 1000

ELSE IF room = "Private" THEN
    charge = 2500

ELSE
    charge = 0

END IF

bill = days * charge

IF bill >= 50000 THEN
    category = "High Cost"

ELSE IF bill >= 20000 THEN
    category = "Medium Cost"

ELSE
    category = "Low Cost"

END IF

PRINT patient_name
PRINT bill
PRINT category

STOP
```

## Source Code 

```python
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
```

## Test Cases

| Test Case | Room Type | Days | Expected Bill | Category |
|---|---|---:|---:|---|
| 1 | General | 5 | ₹5,000 | Low Cost |
| 2 | General | 20 | ₹20,000 | Medium Cost |
| 3 | Private | 10 | ₹25,000 | Medium Cost |
| 4 | Private | 20 | ₹50,000 | High Cost |
| 5 | Private | 25 | ₹62,500 | High Cost |
| 6 | General | 50 | ₹50,000 | High Cost |

### Test Case Calculations

**Test Case 1:**
- Room: General
- Days: 5
- Calculation: 5 × 1000 = ₹5,000
- Result: Low Cost

**Test Case 2:**
- Room: General
- Days: 20
- Calculation: 20 × 1000 = ₹20,000
- Result: Medium Cost

**Test Case 3:**
- Room: Private
- Days: 10
- Calculation: 10 × 2500 = ₹25,000
- Result: Medium Cost

**Test Case 4:**
- Room: Private
- Days: 20
- Calculation: 20 × 2500 = ₹50,000
- Result: High Cost

## Sample Outputs

### Output 1: General Room – Low Cost

```text
Enter patient name: Rahul
Enter number of days: 5
Enter room type (General/Private): General

Patient Name: Rahul
Total Bill: Rs. 5000
Patient Category: Low Cost
```

### Output 2: General Room – Medium Cost

```text
Enter patient name: Priya
Enter number of days: 20
Enter room type (General/Private): General

Patient Name: Priya
Total Bill: Rs. 20000
Patient Category: Medium Cost
```

### Output 3: Private Room – Medium Cost

```text
Enter patient name: Arun
Enter number of days: 10
Enter room type (General/Private): Private

Patient Name: Arun
Total Bill: Rs. 25000
Patient Category: Medium Cost
```

### Output 4: Private Room – High Cost

```text
Enter patient name: Vennela
Enter number of days: 20
Enter room type (General/Private): Private

Patient Name: Vennela
Total Bill: Rs. 50000
Patient Category: High Cost
```

## Conclusion

The Hospital Billing and Patient Classification System successfully calculates hospital bills based on the patient's room type and number of hospital days.

The project uses basic Python concepts such as input statements, print statements, arithmetic operators, and conditional statements like if, elif, and else.

It helps to reduce manual calculation errors and makes hospital billing easier.
