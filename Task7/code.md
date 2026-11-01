## Problem Statement

The Retail Billing System is designed to calculate the final shopping bill based on the total purchase amount and applicable discount.

The system takes the customer name and shopping amount as input. It checks the shopping amount and provides a discount based on different purchase ranges.

The discount rules are:

- Shopping amount ₹5,000 and above: 20% discount.
- Shopping amount ₹3,000 and above: 15% discount.
- Shopping amount ₹1,000 and above: 10% discount.
- Shopping amount below ₹1,000: No discount.

After calculating the discount, the system subtracts it from the original amount and displays the final bill.

## Objectives

1. To calculate shopping bills automatically.
2. To provide discounts based on purchase amounts.
3. To reduce manual billing calculations.
4. To calculate the final amount after discount.
5. To display the customer's shopping details.
6. To understand conditional statements in Python.

##  Assumptions

1. The customer enters a valid name.
2. The shopping amount is entered as a whole number.
3. The shopping amount cannot be negative.
4. A 20% discount is given for purchases of ₹5,000 and above.
5. A 15% discount is given for purchases of ₹3,000 and above.
6. A 10% discount is given for purchases of ₹1,000 and above.
7. No discount is given for purchases below ₹1,000.
8. No additional taxes or charges are included.

## Algorithm

**Step 1:** Start the program.

**Step 2:** Enter the customer name.

**Step 3:** Enter the shopping amount.

**Step 4:** Check the shopping amount.

**Step 5:** If the amount is greater than or equal to ₹5,000, calculate a 20% discount.

**Step 6:** If the amount is greater than or equal to ₹3,000, calculate a 15% discount.

**Step 7:** If the amount is greater than or equal to ₹1,000, calculate a 10% discount.

**Step 8:** Otherwise, set the discount to zero.

**Step 9:** Calculate the final amount.

Final Amount = Original Amount − Discount

**Step 10:** Display the customer name.

**Step 11:** Display the original amount.

**Step 12:** Display the discount.

**Step 13:** Display the final bill.

**Step 14:** Stop the program.

## Flowchart 

```mermaid id="retail527"
garph TD
    A([Start]) --> B[/Enter Customer Name/]
    B --> C[/Enter Shopping Amount/]
    C --> D{Amount >= 5000?}

    D -- Yes --> E[Discount = Amount * 20%]
    D -- No --> F{Amount >= 3000?}

    F -- Yes --> G[Discount = Amount * 15%]
    F -- No --> H{Amount >= 1000?}

    H -- Yes --> I[Discount = Amount * 10%]
    H -- No --> J[Discount = 0]

    E --> K[Final Amount = Amount - Discount]
    G --> K
    I --> K
    J --> K

    K --> L[/Display Customer Name/]
    L --> M[/Display Original Amount, Discount and Final Bill/]
    M --> N([Stop])
```

## Pseudocode

```text
START

INPUT customer_name
INPUT amount

IF amount >= 5000 THEN
    discount = amount * 0.20

ELSE IF amount >= 3000 THEN
    discount = amount * 0.15

ELSE IF amount >= 1000 THEN
    discount = amount * 0.10

ELSE
    discount = 0

END IF

final_amount = amount - discount

PRINT customer_name
PRINT amount
PRINT discount
PRINT final_amount

STOP
```

##  Source Code

```python
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
```

## Test Cases

| Test Case | Shopping Amount | Discount | Expected Final Bill |
|---|---:|---:|---:|
| 1 | ₹500 | ₹0 | ₹500 |
| 2 | ₹1,000 | ₹100 | ₹900 |
| 3 | ₹2,000 | ₹200 | ₹1,800 |
| 4 | ₹3,000 | ₹450 | ₹2,550 |
| 5 | ₹4,000 | ₹600 | ₹3,400 |
| 6 | ₹5,000 | ₹1,000 | ₹4,000 |
| 7 | ₹6,000 | ₹1,200 | ₹4,800 |

### Test Case Explanation

**Test Case 1:**
- Customer Name: Rahul
- Shopping Amount: ₹500
- Discount: ₹0
- Final Bill: ₹500

**Test Case 2:**
- Customer Name: Priya
- Shopping Amount: ₹1,000
- Calculation: 1,000 × 10% = ₹100
- Final Bill: ₹900

**Test Case 3:**
- Customer Name: Arun
- Shopping Amount: ₹3,000
- Calculation: 3,000 × 15% = ₹450
- Final Bill: ₹2,550

**Test Case 4:**
- Customer Name: Vennela
- Shopping Amount: ₹5,000
- Calculation: 5,000 × 20% = ₹1,000
- Final Bill: ₹4,000

##  Sample Outputs

### Output 1: No Discount

```text
Enter customer name: Rahul
Enter shopping amount: 500

Customer Name: Rahul
Original Amount: 500
Discount: 0
Final Bill: Rs. 500
```

### Output 2: 10% Discount

```text
Enter customer name: Priya
Enter shopping amount: 1000

Customer Name: Priya
Original Amount: 1000
Discount: 100.0
Final Bill: Rs. 900.0
```

### Output 3: 15% Discount

```text
Enter customer name: Arun
Enter shopping amount: 3000

Customer Name: Arun
Original Amount: 3000
Discount: 450.0
Final Bill: Rs. 2550.0
```

### Output 4: 20% Discount

```text
Enter customer name: Vennela
Enter shopping amount: 5000

Customer Name: Vennela
Original Amount: 5000
Discount: 1000.0
Final Bill: Rs. 4000.0
```

## Conclusion

The Retail Billing System successfully calculates the final shopping bill by applying different discount percentages based on the purchase amount.

The project uses basic Python concepts such as input statements, output statements, arithmetic operators, variables, and conditional statements (if, elif, and else).

It helps to reduce manual calculations and makes the billing process simple and efficient.

