# Week 3 Assignment - Discount Calculator

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies discount if it's 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Original price: {final_price}")
