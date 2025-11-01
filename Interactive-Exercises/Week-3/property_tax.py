# This program displays property taxes.
def main():
    
    TAX_FACTOR = 0.0065 # Represents the tax factor.

    # Get the first lot number.
    print('Enter the property lot number or enter 0 to end.')
    lot = int(input('Lot Number: '))

    # Continue processing as long as the user
    # does not enter lot number 0

    while lot != 0:
        # Get the property tax
        value = float(input('Enter the property value: '))

        # Calculate the property tax.
        tax = value * TAX_FACTOR

        # Display the tax.
        print(f'Property tax: ${tax:,.2f}')

        # Display the tax.
        print('Enter the next lot number or enter 0 to end.')
        lot = int(input('Lot Number:'))

main()
