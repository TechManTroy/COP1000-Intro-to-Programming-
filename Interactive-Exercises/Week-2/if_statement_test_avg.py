


#Get the first test score
#Get the second test score
#Get the third test score
#Calculate the average
#Display the average
# If THe average is greater than 95:
#  Congradulate the user

def main():
    testOne = int(input('Enter your first test score: ')) #Get test one
    testTwo = int(input('Enter your second test score: ')) #Get test two
    testThree = int(input('Enter your third test score: '))#Get test three

    # Create constant variable for amount of test that can be inputed
    TEST_QUANITY = 3

    # Create constant variable for high score
    HIGH_SCORE = 95

    # Get the average of all test.
    testAverage = (testOne + testTwo + testThree) / TEST_QUANITY

    # Display average
    print('Your average score is', testAverage)

    #Declare if statement if test is greater than 95.
    if testAverage > HIGH_SCORE:
        print('Congrats!')
        print('You have a average above 95')
        
main()
