# Troy Edmonds
# 2576081
# COP1000
# Colaboration: none


# START

# Loop
    # DEFINE loop FOR integer in RANGE 5 through 50 in increments
    # of 5
    # CALCULATE square root of integer
    # CALCULATE cube root og integer


#Output
    # PRINT headers
    # Display results using f-string
    # INIT(integers) should be centered and 7 characters wide
    # SQUARES column should be right-aligned and 8 characters wide
    # CUBE column should be right aligned and 12 characters wide

# END


def main():

    print(f"{'INIT':^7}{'SQUARES':>8}{'CUBES':>12}")
    print('---------------------------')

    



    for integer in range(5, 51, 5):
        square = integer ** 2
        cube = integer ** 3
        print(f'{integer:^7,}{square:>8,}{cube:>12,}')


main()

    

    
