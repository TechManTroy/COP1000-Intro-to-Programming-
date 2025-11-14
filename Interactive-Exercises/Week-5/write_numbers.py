# This program demonstrates how numbers
# must be converted to strings before they
# are written to a text file.

def main():
    # Open a file for writing
    outfile = open('numbers.txt' , 'w')

    # Get threee numbers from the user.
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the another number: '))
    num3 = int(input('Enter the another number: '))

    # Write the number to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Close the file
    outfile.close
    print('Data has be written to numbers.txt')

if __name__ == '__main__':
    main()
          
         
          
    
