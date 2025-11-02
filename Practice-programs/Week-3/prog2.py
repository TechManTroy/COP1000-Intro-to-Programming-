# Troy Edmonds
# 2476081
# COP1000
# Colaborations: Google Gemini

#START

#input
    # SET input to variable number
    # PROMT user for "Enter your number or 0 to quit:"
        # Convert to integer

# Determine whether number is even or odd
    # WHILE number != 0:
        # IF number % 2 == 0
        # DISPLAY "This number is even"
    # ELSE
        # DISPLAY "This number is odd"
# input
    # GET next number
    # PROMT user for "Do you have another number?
    # (or hit 0 to quit)"

# output
    # DISPLAY "Goodbye" if program is closed 






def main():
    # Get user input
    number = int(input('Please input your number'+
                       '(or hit 0 to quit): '))

    # Ensure loop continues aslong as number is not 0 
    while number != 0:
        # Check if number is odd or even
        if number % 2 == 0:
            print(f'The number {number} is even')
        else:
            print(f'The number {number} is odd')

    # Get next input
        number = int(input('Do you have another number? '+
                         '(Enter 0 to quit): '))

    print('Goodbye')
        
              
              
main()
    
        
    
