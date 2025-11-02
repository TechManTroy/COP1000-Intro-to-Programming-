# Troy Edmonds
# 2576081
# COP1000
# Colaborations:



# START

# Define constants
    #SET conversion factor for U.S. tons
        # TON_CONVERSION_FACTOR = 0.892857143

# Input
    # SET input variable TO start_tons_value
    # PROMT user for "Enter the starting value for US tons: "
    # CONVERT to INTEGER
    # number cannot be a negative number
    # ELSE:
    # Dispalay error if negative number is entered.

    # SET input variable TO stop_tons_value
    # PROMT user for "Enter the ending value for US tons: "
    # CONVERT to INTEGER
    # number cannot be a negative number
    # ELSE:
    # Dispalay error if negative number is entered.

    # SET variable for US tons step to step_for_tons
    # PROMPT user for "Enter the step value for US tons: "
    # CONVERT to INTEGER
    # number cannot be negative
    # ELSE:
    # Dispalay error if negative number is entered.

# Proccess and output
    # OUTPUT formatted table header " US Tons, Imperial Tons
        # US Tons should be centered and 10 characters wide
        # Imperial Tons should be right aligned and 13 characters wide

    # LOOP SET us_tons with range between start_tons_value,
    # stop_tons_value + 1 , with step_tons_value
        # Display us_tons and us_tons * TON_CONVERSION_FACTOR
        # FORMAT us_tons results centered and 10 characters wide
        # FORMAT converted us_tons right aligned and 13 characters wide
        # showing 3 decimal places

    # END LOOP

#END





def main():

    TON_CONVERSION_FACTOR = .892857143 # Convertion factor

    # Get start, stop, and step input from user convert to integer
    # and validate number is not negative
    while(start_tons_value :=int(input('Enter the starting value ' +
                                     'for U.S. tons: '))) <= -1:
        print('Value cannot be a negative number, '
              'please enter a correct value')
    else:
        print(f'The start value for U.S tons: {start_tons_value}')
        print()


    while(stop_tons_value :=int(input('Enter the ending value ' +
                                     'for U.S. tons: '))) <= -1:
        print('Value cannot be a negative number, '
              'please enter a correct value')
    else:
        print(f'The ending value for U.S tons: {stop_tons_value}')
        print()


    while(step_for_value :=int(input('Enter the step value ' +
                                     'for U.S. tons: '))) <= -1:
         print()
         print()


    print(f'{"US Tons":^10}{"Imperial Tons":>13}') #DISPLAY converted table head
    print('-----------------------')


    for us_tons in range(start_tons_value, stop_tons_value + 1, step_for_value):
        print(f'{us_tons:^10}{us_tons * TON_CONVERSION_FACTOR:>13.3}')
    


main()
        














    
