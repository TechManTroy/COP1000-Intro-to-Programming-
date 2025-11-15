# This program promys the user for sales amounts
# and writes those amounts to the sales.txt file

def main():
    # Get the number of days

    num_days = int(input('For how many days do ' +
                         'you have sales? '))

    # Open a new file named sales.txt

    sales_file = open('sales.txt', 'w')

    # Get the amount of sales for each day and write
    # it to the file

    for count in range(1, num_days + 1):
        # Get the sales for a day
        sales = float(input(f'Enter the sales for the day ' +
                            f'#{count}: '))

        # Write the salse amount to the file
        sales_file.write(f'{sales}\n')

    # Close the file
    sales_file.close()

    print('Data has be written to sales.txt')

if __name__ == '__main__':
    main()
