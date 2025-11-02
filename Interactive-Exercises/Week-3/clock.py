# This program demonstrates using nested loops 
def main():
    for seconds in range(60): # Display seconds from 0 through 59
        print(seconds)

    for minutes in range(60): # Loop that cycles through 60 minutes
        for seconds in range(60):
            print(minutes,':', seconds)

    for hours in range(24): # Loop that counts the hours 
        for minutes in range(60):
            for seconds in range(60):
                print(hours, ':', minutes, ':', seconds)
    
main()
