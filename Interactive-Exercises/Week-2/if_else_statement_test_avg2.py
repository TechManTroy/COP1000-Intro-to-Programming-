


# Get the number of hours worked
# Get the hourly pay rate.
# If the employee worked more than 40 hours:
#   Calculate and display the gross pay with overtime
# Else:
#   Calculate and display the gross pay as usual.


def main():
    hoursWorked = float(input('How many hours did you work? '))
    payRate = float(input('What is your pay rate? '))

    #Create constant variable for hours in a week
    HOURS_IN_A_WEEK = 40
    #Create constanr variable for OT multiplyer
    OVERTIME_MULTIPLYER = 1.5

    #calculate total overtime hours
    overtimeHours = hoursWorked - HOURS_IN_A_WEEK

    #calculate gross pay
    grossPay = hoursWorked * payRate

    #calculate total overtime gross pay
    overtimePay = overtimeHours * payRate * OVERTIME_MULTIPLYER

    #calculate gross pay with overtime
    gross_with_overtime = HOURS_IN_A_WEEK * payRate + overtimePay

    #Display results.
    print('Hours:', hoursWorked)

    if hoursWorked <= 40:
        print(f'Gross Pay: ${grossPay:,.2f}')
    else:
        print('Overtime Hours:', overtimeHours)
        print(f'Gross Pay: ${gross_with_overtime:,.2f}')


main()
    
    
    
