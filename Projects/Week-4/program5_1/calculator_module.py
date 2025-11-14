# Troy Edmonds
# 2576081
# COP1000
# Colaboration: Google Gemini

# This is a custom module to hold the function used to calculate 
# the subtotal for a specific type and quanity of quanity of 
# shoestring pairs

# START

# FUNCTION CALCULATE_STRING_SUBTOTAL(EYELET_PAIRS, QUANITY):
    # Define the cost constant
    # SET COST_PER_EYELET_PAIR = 0.50

    # Calculate the price for a sinle pair of shoestings
    # SET SUBTOTAL = PRINCE_PER_SHOESTRING_PAIR * QUANITY

    # RETURN SUBTOTAL
# END FUNCTION

# END


def calculate_string_subtotal(eyelet_pairs: int, quanity: int) -> float:

    # Calculate subtotal for the given quanity of shoestring pairs.

    # The cost calculated based on eyelet pairs, where each pair of
    # eyelets cost $.50

    # Arguments:
        # eyelet_pairs: The number of eyelet pairs (3 to 10)
        # determines length/price

        # quanity: The number of shoesting pairs being purchaced.

    # Returns
        # The calculated subtotal (float).


    COST_PER_EYELET_PAIR = 0.50 # 0.05 per pair of eyelets

    # Calculate the base cost for a single pair of shoestrings
    price_per_shoestring_pair = eyelet_pairs * COST_PER_EYELET_PAIR

    # Calculate the subtotal for the purchaced quanity
    subtotal = price_per_shoestring_pair * quanity

    return subtotal

    



