# This program calculates a retail items sales price

# DISCOUNT_PERCENTAGE is used as a global
# constant for the discount percentage.
DISCOUNT_PERCENTAGE = .20

# The main function.
def main():
    # Get the items regular price.
    reg_price = get_regular_price()

    # Calculate the sales price.
    sales_price = reg_price - discount(reg_price)

    # Display the sales price
    print(f'The sales price is ${sales_price:,.2f}')


# The regular_price function prompts the
# user to enter an items regular price and
# it returns that value.

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

# The discount function accepts an items price
# as an argument and returns the amount of the
# discount, specified by DISCOUNT_PERCENTAGE.
def discount(price):
    return price * DISCOUNT_PERCENTAGE


# Call the main function
main()
