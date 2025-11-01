


# This program gets test score from user and
# decides whether that score is over 90


def main():
    A_SCORE = 90 # minimum score for A
    B_SCORE = 80 # minimum score for B
    C_SCORE = 70 # minimum score for C
    D_SCORE = 60 # minimum score for D

    # Get test score from student
    score = float(input('Enter you test score: '))

    # Determine letter grade for test score
    if score >= A_SCORE:
        print('You have an A for this class.')
    else:
        if score >= B_SCORE:
            print('You have a B for this class.')
        else:
            if score >= C_SCORE:
                print('You have a C for this class.')
            else:
                if score >= D_SCORE:
                    print('You have a D for this class.')
                else:
                    print('You have an F for this class')
                            
    


main()
                  
    
