# This program converts the speeds 60 kph
# $ through 130 kph (in kph increments)
# to mph

def main():
    START_SPEED = 60            # Start speed
    END_SPEED = 131             # Ending speed
    INCREMENT = 10              # Speed increment
    CONVERSION_FACTOR = 0.6214  # Conversion factor

    # Preint the speeds
    for kph in range(START_SPEED, END_SPEED, INCREMENT):
        mph = kph * CONVERSTION_FACTOR
        print(f'{kph}\t{mph.1f}')


main()
