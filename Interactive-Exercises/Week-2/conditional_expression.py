# This program dimonstrates a conditional expression

def main():
    num1 = int(input('Input your first number: '))
    num2 = int(input('Input your second number: '))

    max = num1 if num1 > num2 else num2
    print (f'The bigger number is {max}.')


main()
