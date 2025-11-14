# Troy Edmonds
# 2576081
# COP1000
# Colaborations: Google Gemini



# START

# Define the main function
    # FUNCTION main()
        # Generate two random integers 1 and 5
        # SET random1 TO a random integer between 1 and 5
        # SET random2 TO a random integer between 1 and 5

    # Display the generated numbers
        # DISPLAY "Generated integers: " random1, and random2

    # Call the show_larger function with the generated numbers
        # CALL show_larger(random1, random2)
    # END FUNCTION

# Define the show_larger function
    # FUNCTION show_larger(number1, number2)
        # Determine the positive difference
        # SET diff TO ABS(number1 - number2)

        # Check if numver are equal
        # IF diff is Equal to 0 THEN
            # Display results for equal numbers
            # DISPLAY "Both" number1 "and" number2 "are the same"
        # ELSE
            # Determine the larger number
            # SET larger to MAX(number1, number2)
            # Determine tht smaller number
            # SET smaller to MIN(number1, number2)

            # Display results
            # DISPLAY "The larger integer is" + larger
            # DISPLAY "It is larger than" + smaller "by a difference of"
            # + diff

        # END IF
    # END FUNCTION

    # Start execution of program
    # IF __name__ == "__main__":
        # Call main()

# END
            

    
import random

def main():
    # Generate two random integers in between ranges [1,5]
    random1 = random.randint(1,5)
    random2 = random.randint(1,5)

    # Display random generated numbers 
    print(f'Generated integers: {random1} and {random2}')

    # Call the show_larger function
    show_larger(random1, random2)

    


# Define show larger function
def show_larger(number1, number2):

    # Determine the positive difference
    diff = abs(number1 - number2)

    # Determine if numbers are equal, larger, or smaller than one another
    if diff == 0:
        print(f'Both {number1} and {number2} are the same')
    else:
        # Determine the larger and smaller number
        larger = max(number1, number2)
        smaller = min(number1, number2)

        # Display results
        print(f'The larger integer is {larger}')
        print(f'It is larger than {smaller}' +
              f' by a difference of {diff}')

# Call the main function 
if __name__ == "__main__":
    main()

        
