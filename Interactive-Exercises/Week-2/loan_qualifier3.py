# This program determines whether a bank customer
# qualifies for a loan.




def main():
    MIN_SALARY = 30000 # The minimum annual salary
    MIN_YEARS = 2 # The minimum years on the job

    # Get customer salaryu and years worked

    salary = float(input('Enter your salary: '))
    years = int(input('Enter your years on the job: '))

    # Determine is customerr qualifies

    if salary >= MIN_SALARY or years >= MIN_YEARS:
        print(f'You qualify for a loan.')
    else:
        print(f'Sorry, you do not qualify for a loan.')



main()

    
