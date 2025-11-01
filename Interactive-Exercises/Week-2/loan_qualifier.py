

# This program determines whether a bank customer
# qualifies for a loan

def main():
    MIN_SALARY = 30000.0 # The minimum annual salary
    MIN_YEARS = 2 # The minimum years on the job

    # Get the customers annual salary
    salary = float(input('Enter you salary: '))

    # Get the numver of years worked on a job
    years_on_job = int(input('Enter the years employed: '))

    # Determin if customer qualifies for loan
    if salary >= MIN_SALARY:
        if years_on_job >= MIN_YEARS:
            print('You qualify for a loan')
        else:
            print(f'You must have been qualified '
                  f'for at least {MIN_YEARS} '
                  f'years to qualify')

    else:
        print(f'You must earn at least $'
              f'{MIN_SALARY:,.2f} '
              f'per year to qualify.')

    
main()                   
