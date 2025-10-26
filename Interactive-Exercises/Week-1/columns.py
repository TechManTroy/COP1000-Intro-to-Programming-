# This program displays the following numbers
# in two columns
def main():
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999

# Each number is displaued in a field of 10 spaces
# and rounded to 2 decimal places

    print(f'{num1:10.2f}{num2:10.2f}')
    print(f'{num3:10.2f}{num4:10.2f}')
    print(f'{num5:10.2f}{num6:10.2f}')

main()
