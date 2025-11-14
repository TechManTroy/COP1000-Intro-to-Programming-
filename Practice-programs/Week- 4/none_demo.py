# This program demonstrates the None keyword.

def main():
    # Get two numbers from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # Call the divide function.
    quotient = divide(num1, num2)

    # Display the result.
    if quotient is None:
        print('Cannot divide by zero.')
    else:
        print(f'{num1} divide by {num2} is {quotient}. ')

# The divide function divides num1 by num2 and
# returns the result. If num2 is 0,
# return None.
def divide(num1, num2):
    if num2 == 0:
        result = None
    else:
        return num1 / num2
    return result

# Call the main function.
main()

        
        
