# Troy Edmonds
# 2476081
# COP1000
# Colaborations: None

# START

# Input
# SET INPUT variable one TO first_read
# PROMT user "Enter the first blood sugar reading after fasting in mg/dl:"
# SET INPUT variable one TO second_read
# PROMT user "Enter the second blood sugar reading after fasting in mg/dl:"
# SET INPUT variable one TO third_read
# PROMT user "Enter the third blood sugar reading after fasting in mg/dl:"


# Identify highest reading
# IF first_read < third_read  and second_read < third_read
  # SET lowest_total TO first_read + second_read
# ELSE IF first_read < second_read and third_read < second_read
  # SET lowest_total TO first_read + third_read
# ELSE IF second_read < first_read and third_read < first_read
  # SET lowest_total TO second_read + third_read
# END IF

# Calculate average of two lowest readings
# IF (average_of_lowest := lowest_average / 2)
#   PRINT "Your average blood sugar is {average_of lowest} mg/dl




# GET input from the user 
def main():
    first_read = int(input('Enter first blood sugar reading after fasting in mg/dL: '))
    second_read = int(input('Enter second blood sugar reading after fasting in mg/dL: '))
    third_read = int(input('Enter third blood sugar reading after fasting in mg/dL: '))

# Determine which two readings are the lowest then ADD them
    if first_read < third_read  and second_read < third_read:
        lowest_total = first_read + second_read
    elif first_read < second_read and third_read < second_read:
        lowest_total = first_read + third_read
    elif second_read < first_read and third_read < first_read:
        lowest_total = second_read + third_read


    if (average_of_lowest := lowest_total / 2):
        print(f'Your average blood sugar is {average_of_lowest} mg/dL')


main()



        


    


