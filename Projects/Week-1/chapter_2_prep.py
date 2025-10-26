# Troy Edmonds
# 2576081
# COP1000
# Contributions: None


# Pseudocode
# 1. Define main body
# 2. Get score for test 1
# 3. Get score for test 2
# 4. Get score for test 3
# 5. Convert scores into float so we can use decimals
# 6. Create average variable and assign steps 7 and 8
# 7. Add scores from test1, test2, and test3
# 8. Divide total by 3(total number of test)
# 9. Display results as a percentage with only two decimals 




#Setting up enviorment and creating variables 

def main():
    test1 = float(input('Enter your first test score: '))
    test2 = float(input('Enter your second test score: '))
    test3 = float(input('Enter your third test score: '))

   
    average = (test1 + test2 + test3) / 3  #calcutate average of test scores

    
    print(f'The average of these scores is {average:.2f}%') #display results

main()
