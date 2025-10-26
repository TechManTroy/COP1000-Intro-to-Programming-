# Troy Edmonds
# 2576081
# COP1000
# Collaborations: none

# START

# 1.CREATE enviorment by defining the MAIN body.
# 2.GET total hours, store in variable named total_hours.
# 3.COVERT to INTEGER 
# 4. CREATE variable named total_days
# 5. CREATE constant variable named HOURS_IN_A_DAY asign 
#    24
# 6. GET total days by DIVIDING total_hours BY      
#    HOURS_IN_A_DAY.
#    using // since working with float numbers.
#    store in total_days.
# 7. CREATE variable for final hours named final_hours.
# 8. GET total number of remaining hours by 
#    USING modulous to GET remainder of total_hours BY #    HOURS_IN_A_DAY store in 
#    variable named final_hours.   
# 9. Display results.

# END


def main():
    # get total hours from user

    total_hours = int(input('What is the number of hours to convert to days\
 and hours? '))
    # Define Variable constant for number of hours in a 
    # day 
    HOURS_IN_A_DAY = 24

    # get the total days
    
    total_days = (total_hours // HOURS_IN_A_DAY)

    # get number of remaining hours

    final_hours = total_hours % HOURS_IN_A_DAY

    # display result

    print(total_hours, 'hours is equivalent to' , total_days ,'days(s) and' , final_hours ,'hours(s)')

main()