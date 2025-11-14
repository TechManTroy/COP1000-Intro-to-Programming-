# Troy Edmonds
# 2576081
# COP1000
# Colaborations: Google Gemini

# This is the main program for the shoestring check out system

#START

# Initialize the main total
# SET Total_cost = 0.0

# Prompt for the number of differnet tyoes to purchase.

# DISPLAY "Enter the number of different types of shoestrings being purchaced
# INPUT num_types to INTEGER

# Handle zero or negative purchases

    # IF num_types <= 0 THEN
        # DISPLAY "No items purchased. Thank you!"
        # EXIT PROGRAM
    # END IF

# Loop through each distinct type of shoestring purchase
    # FOR i FROM 1 TO num_types:
        # DISPLAY "--- Item Type " + i + " of " + num_types + " ---"

        # Get and validate eyelet type
        # DISPLAY "Enter the number of eyelet pairs (3-10) for this type: "
        # INPUT eyelets
        # CONVERT eyelets TO INTEGER

        # IF eyelets < 3 OR eyelets > 10 THEN
            # DISPLAY "Error: Eyelet pairs must be between 3 and 10. Skipping this item."
            # CONTINUE LOOP // Skip to the next iteration
        #END IF

        # Get and validate quantity
        # DISPLAY "Enter the quantity (number of shoestring pairs) being purchased: "
        # INPUT quanity
        # CONVERT quanity TO INTEGER

        # IF quanity < 0 THEN
            # DISPLAY "Error: Quantity cannot be negative. Skipping this item."
            # CONTINUE LOOP // Skip to the next iteration
        # END IF

        # Calculate subtotal using the imported function
        # SET SUBTOTAL = CALCULATE_SHOESTRING_SUBTOTAL(EYELETS, QUANTITY)

        # Display subtotal and accumulate total cost
        # DISPLAY "Subtotal for Item " + I + ": " + FORMAT_AS_CURRENCY(SUBTOTAL)
        # TOTAL_COST = TOTAL_COST + SUBTOTAL
    # END FOR

# Display final results
    # DISPLAY "========================================"
    # DISPLAY "Total Cost of Purchase: " + FORMAT_AS_CURRENCY(TOTAL_COST)
    # DISPLAY "========================================"
    # DISPLAY "Thank you for shopping at Shoestring Store!"

# END PROGRAM

# Import the custom function from the separate mofule file
from calculator_module import calculate_string_subtotal

# Controls the main logic of the program
def main():
    print('--- Shoesting Store Checkout System ---') # Header

    # Initialize the total cost accumulator
    total_cost = 0.0

    # Promt for the number of shoestring types being purchaced
    num_types = int(input('Enter the mumber of different types of' +
                          ' shoestings being purchaced: '))
    if num_types <= 0:
        print('No items purchaced. Thank you!')
        return

    # Loop through each type of shoestring purchase
    for i in range(1, num_types + 1):
        print(f'\n--- Item Types {i} of {num_types} ---')

        # Get the type (number of eyelets)
        eyelets = int(input('Enter the number of eyelet pairs' +
                            '(3-10) for this type: '))

        # Validate eyelet range
        if not 3 <= eyelets <= 10:
            print('Error: the eyelet pairs must be between' +
                  '3 and 10. Skip to next item.')
            continue

        # Get quanity
        quanity = int(input('Enter the quanity (number of shoesting)'+
                            ' being purchaced: '))

        # validate quanity
        if quanity < 0:
            print('Error: Quanity cannot be negative. Skipping this item.')
            continue

        # Pass the values to the custom function to get subtotal
        subtotal = calculate_string_subtotal(eyelets, quanity)

        # Print the subtotal for current item and accumulated cost
        total_cost += subtotal

    # Print final cost
    print('\n' + '=' * 40) # Top of final results footer
    # The final total cost is reported in currency format
    print(f'Total Cost of Purchace: ${total_cost:.2f}')
    print('='*40)# Bottom og final results footer
    print('Thank you for shoping at Shoestring Store!')

if __name__ == "__main__":
          main()


                            
    
