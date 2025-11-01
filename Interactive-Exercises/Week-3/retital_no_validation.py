# This program  calculates ratail prices. 
def main():
    MARK_UP = 2.5 # The marke up percentage
    another = 'y' # Variable to control loop.

    # Process one or more items
    while another == 'y' or another == 'Y':

    # Get the item's wholesale cost.
        wholesale = float(input("Enter the item's wholesale cost: "))

    # Calculate the retail price
        retail = MARK_UP * wholesale

    # Display the retail price.
        print (f'Retail proce: ${retail:,.2f}')

    # Do it again.
        another = input('Do you have another item? '+
                    '(Enter y for yes): ')
    
main()
