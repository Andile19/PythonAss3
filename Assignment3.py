# Quesition 1
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or more.
    
    Parameters:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage to be applied.
        
    Returns:
        float: Final price after applying discount, or original price if discount < 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price
#Question 2
# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied. Final price: ${final_price:.2f}")
    else:
        print(f"No discount applied. Final price: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")
