# This program calculates the sum of a series
# of numbers entered by the user.

def main():

    MAX = 5 # The maximum number

    # Initialize an accumulator variable.
    total = 0.0

    # Explain what we are doing.
    print('This prigram calculates the sum of ', end='')
    print(f'{MAX} numbers you will enter.')

    # Get the numbers and accumulate them.
    for counter in range(MAX):
        number = int(input('Enter a number: '))
        total = total + number

    print(f'The total is {total}.')

main()
