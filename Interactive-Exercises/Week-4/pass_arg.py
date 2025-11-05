# This program demonstrates an argument being
# passed to a funtion.


def main():
    value = 5
    show_double(value)


# The show_double funtion accepts an argument
# and displays double its value.

def show_double(number):
    result = number * 2
    print(result)


# Call main function
main()
