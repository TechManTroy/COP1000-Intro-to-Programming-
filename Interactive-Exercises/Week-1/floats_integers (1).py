# Get the users hours, convert to integer.
hours = int(input('How many hours did you work? '))
print(hours)

# Get the users pay rate, convert to float.
pay_rate = float(input('What is your pay rate? '))
print(pay_rate)

print('Here is your net pay')
print(hours * pay_rate)
