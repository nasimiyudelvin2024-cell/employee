# supermarket_discount.py
# Applies a 15% discount for purchases of KSh 10,000 or more

# --- Get input from user ---
purchase_amount = float(input("Enter total purchase amount: "))

# --- Check eligibility using comparison operator ---
qualifies = purchase_amount >= 10000

if qualifies:
    discount = 0.15 * purchase_amount
    final_amount = purchase_amount - discount
else:
    discount = 0.0
    final_amount = purchase_amount

# --- Display results ---
print(f"Purchase Amount: {purchase_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Amount: {final_amount:.2f}")
