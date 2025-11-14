# Troy Edmonds
# 2576081
# COP1000
# Colaborations: Google Gemini


# START

# IMPORT MODULE
    # IMPORT program5_2 and p52

# FUNCTION main():
    # DISPLAY '--- Module-Based Cubiod Geometry Calculator
            # '(using program5_2 ---'

    # Input: Get demensiond from the user
    # DISPLAY 'Please enter the demensions of the
            # 'rectangular cubiod:'
    # INPUT length as a float
    # INPUT width as a float
    # INPUT height as a float

    # DISPLAY '\n--- Results ---'

    # Calculate and display Surface Area
    # Call the imported function from the p52 module
    # SET diagonal = p52.calculate_surface_area
    # (length, width, height)
    # DISPLAY 'Surface Area: ' + surface_area
    # ( formatted to 3 decimals)    

    # Calculate and display Diagonal
    # Call the imported function from the p52 module
    # SET diagonal = p52.calculate_diagonal(length, width, height)
    # DISPLAY 'Diagonal: ' + diagonal ( formatted to 3 decimals)

    # Calculate and print Volume
    # Call the imported function ( handles its own printing)
    # p52.calculate_volume(length, width, height)

    # DISPLAY '-----------------------'
# END FUNCTION

# Call the main function
# IF __name__ == "__main__":
    # main()

# END PROGRAM
    
    



# Import the entire program5_2 script as a module
import program5_2 as p52 # assign alias for easy use 

def main():

    #Title
    print('--- Module-Based Cubiod Geometry Calculator' +
          ' (using program5_2)')


    # Prompt the user for demensions and executes the imported
    # functions from the program5_2 to display results.
    print('\nPlease enter the deminsions of the rectangular cubiod:')
    length = float(input('Enter the length (l) of the cubiod: '))
    width = float(input('Enter the width (w) of the cubiod: '))
    height = float(input('Enter the height (h) of the cubiod: '))


    # Header
    print('\n--- Results ---')

    # Calculate and display Surface Area (4 decimals)
    # Call the function from imported module
    surface_area = p52.calculate_surface_area(length, width, height)
    print(f'Surface Area: {surface_area:.4f}')

    # Calculate and display Diagonal (3 decimals)
    diagonal = p52.calculate_diagonal(length, width, height)
    print(f'Diagonal: {diagonal:.3f}')

    # Calculate and print Volume (3 decimals)
    # This function handles its own printing internally as defined
    # in program5_2
    p52.calculate_volume(length, width, height)

    # Footer
    print('----------------')

if __name__ == "__main__":
    main()

          

    
    

          
    
