# Troy Edmonds
# 2576081
# COP1000
# Coaborations: Google Gemini

# This program calculates the surface area, volume, and diagonal
# of a rectangular cuboid(box) using seperate custom functions.

# START

# Key: l = length , w = width , h = height

# FUNCTION main():
    # DISPLAY '--- Rectangular Cubiod Geometry Calculator ---'

    # Get input demensions (l, w, h)
    # INPUT l as a float
    # INPUT w as a float
    # INPUT h as a float

    # DISPLAY 'n\--- Results ---'

    # Calculate and diaplay Surface Area
    # SET surface_area = calculate_surface_area(l, w, h)
    # DISPLAY 'Surface Area: ' + Surface_area (format to 4 decimals)

    # Calculate and display Diagonal
    # SET diagonal = calculate_diagonal(l ,w, h)
    # DISPLAY 'Diagonal: ' + diagonal (formatted to 3 decimals)

    # Calculate and display Volume(handled inside the function)
    # calculate_volume(l, w, h)

    # DISPLAY '---------------'
# END FUNCTION

# FUNCTION calculate_surface_area(l, w, h):
    # FORMULA: 2lw + 2lh + 2hw 
    # SET area = 2 * ( l * w + l * h + w * h)
    # RETURN area rounded to 4 decimal places

# END FUNCTION

# FUNCTION calculate_diagonal(l, w, h):
    # FORMULA: √(l² + w² + h²)
    # SET sum_of_squares = l^2 + w^2 + h^2
    # SET diagonal = sqrt(sum_of_squares)
    # RETURN diagonal rounded to 3 decimal places
# END FUNCTION

# FUNCTION calculate_volume(l, w, h)(Void function):
    # FORMULA: lwh
    # SET volume = l * w * h
    # DISPAY 'Volume: ' + volume rounded to 3 decimal places
# END FUNCTION

# CALL main function
# IF __name__ == "__main__":
    # main()

# END PROGRAM



import math


# Main Executing Function
def main():
    # Header
    print( '--- Rectangular Cubiod Geometry Calculator ---')

    # Promt the user for cubiod dementions
    length = float(input('Enter the length (l) of the cubiod: '))
    width = float(input('Enter the width (w) of the cubiod: '))
    height = float(input('Enter the height (h) of the cubiod: '))

    print('\n--- Results ---') # Display inputted results

    # Calculate / Call and display the Surface Area
    # showing 4 decimals
    surface_area = calculate_surface_area(length, width, height)
    print(f'Surface Area: {surface_area:.4f}')

    # Calculate / Call and display Diagonal
    # showing 3 decimals
    diagonal = calculate_diagonal(length, width, height)
    print(f'Diagonal: {diagonal:.3f}')
    
    # Calculate / Call and display Diagonal
    # showing 3 decimals
    # print handled inside the custom function
    calculate_volume(length, width, height)

    # Footer
    print('-----------------------')



# Custom Functions for Calculating area
# hint that length, width, and height are expected floats
def calculate_surface_area(length: float, width: float,
                           height: float) -> float:

    # Formula for area: 2 * (l*w + l*h + w*h)
    area = 2 * (length * width + length * height + width * height)

    # Return the value accurate to four decimal places
    return round(area, 4)


# Custom Functions for Calculating the diagonol 
# length of a rectangular cubiod returns float
def calculate_diagonal(length: float, width: float,
                           height: float) -> float:
    
    # Formula to calculate sum of squares: sqrt(l^2 + w^2 + h^2)
    sum_of_squares = length**2 + width**2 + height**2

    # Calculate the square root using math.sqrt()
    diagonal = math.sqrt(sum_of_squares)

    # Return value accurate to three decimal places
    return round(diagonal, 3)



# Calculate the colume of a rectangular cubiod (lwh)
# and prints the results (Void function) returns NONE
def calculate_volume(length: float, width: float,
                     height: float) -> None:

    # Formula for volume: l * w * h
    volume = length * width * height

    # print volume, accurate to three decimal places.
    print(f'Volume: {volume:.3f}')


if __name__ == "__main__":
    main()
    
