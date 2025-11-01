# Troy Edmonds
# 2476081
# COP1000
# Colaborations: None 

# START

# Define Constants
  # SET GUITAR_PICK_PRICE TO .25
  # SET ONE_DOZEN_PRICE TO .23
  # SET TWO_DOZEN_PRICE TO .21
  # SET THREE_DOZEN_PRICE TO .19

# Input
  # SET INPUT variable TO pick_quanity
  # PROMT user for "How many guitar picks are you ordering?"
      #CONVERT to INTEGER

# Determine cost and discount per quanity
  # IF pick_quanity > 36 THEN
  #    SET pick_cost and MULTIPLY pick_quanity BY THREE_DOZEN_PRICE
  # ELSE IF pick_quanity > 24 THEN
  #    SET pick_cost and MULTIPLY pick_quanity BY TWO_DOZEN_PRICE
  # ELSE IF pick_quanity > 12 THEN
  #    SET pick_cost and MULTIPLY pick_quanity BY ONE_DOZEN_PRICE
  # ELSE
  #    SET pick_cost and MULTIPLY pick_quanity BY GUITAR_PICK_PRICE
  # END IF

# Output
  # SET total_cost
  # DISPLAY "Total cost of guitar picks: $ +FORMAT{total_cost, 2 decimal places)

# END


def main():
    GUITAR_PICK_PRICE = .25 # Base price for guitar picks
    ONE_DOZEN_PRICE = .23 # Price for one dozen of more guitar picks 
    TWO_DOZEN_PRICE = .21 # Price for two dozen of more guitar picks 
    THREE_DOZEN_PRICE = .19 # Price fo three dozen guitar picks

    # Get quanity of guitar picks from user
    pick_quanity = int(input('How many guitar picks are you purchasing? '))

    # Calculate cost per quanity and apply discount per dozen
    if pick_quanity > 36:
        pick_cost = pick_quanity * THREE_DOZEN_PRICE
    elif pick_quanity > 24:
        pick_cost = pick_quanity * TWO_DOZEN_PRICE
    elif pick_quanity > 12:
        pick_cost = pick_quanity * ONE_DOZEN_PRICE
    else:
        pick_cost = pick_quanity * GUITAR_PICK_PRICE

    # Display total cost of guitar picks

    print(f'The total cost of your gutair picks: ${pick_cost:,.2f}')


main()
    
