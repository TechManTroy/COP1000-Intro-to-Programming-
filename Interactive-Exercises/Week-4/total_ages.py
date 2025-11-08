# This progeam uses the return value function.

def main():
    # Get the user's age.
    first_age = int(input('Enter your age: '))

    # Get the users best friens's age
    second_age = int(input("Enter your best friend's " +
                           'age: '))

    # Get the sum of both ages
    total = sum(first_age, second_age)

    # Display total age
    print(f'Together you are {total} years old')



# The sum function accepts teo numeric arguments and
# returns the sum of those areguments

def sum(num1, num2):
    results = num1 + num2
    return results

# Call the main funnction
main()
