# Troy Edmonds
# 2576081
# COP1000
# Colaboration: Google Gemini for help with pseudocode and small logic errors

# START



#1. Define Constants
    # SET PRICE_OVER_40 TO 7.50
    # SET PRICE_OVER_20 TO 8.75
    # SET PRICE_OVER_10 TO 10.00
    # SET PRICE_ONE_TO_NINE TO 12.00
    # SET SALES_TAX_RATE TO 0.07 // 7%
    # SET SHIPPING_RATE_PER_POUND TO 1.00 // $1 PER POUND

#2. Input
    # PROMPT user for "How many pounds you would like to order?"
    
#3. Determine Price Per Pound
    # SET price_per_pound TO 0.00

    # IF pounds > 40 THEN
    #   SET price_per_pound TO PRiCE_OVER_40
    # ELSE IF pounds > 20 THEN
    #   SET price_per_pound TO PRICE_OVER_20
    # ELSE IF pounds > 9
    #   SET price_per_pound TO PRICE_OVER_10
    # ELSE
    #   SET price_per_pound TO PRICE_ONE_TO_NINE
    # END IF

#4. Calculate Base Cost
    # SET cost_cofee TO pounds * price_per_pound
    # DISPLAY "Your cost of coffee is $" + FORMAT(cost_coffee, 2 decimal places)

#5. Calculate Sales Tax
    # SET sales_tax TO cost_coffee * SALES_TAX_RATE
    # DISPLAY "Your cost of coffee is $" + FORMAT(cost_coffee, 2 decimal places)

#6. Calculate Shipping
    # SET shipping to 0.00

    # IF cost_cofee > 150 THEN
    #   SET shipping TO 0.00
    #   DISPLAY "Shipping fee: $0.00 (Free shipping!)"
    # ELSE
    #   SET shipping_fee To SHIPPING_RATE_PER_POUND * pounds
    #   DISPLAY "Shipping fee: $" + FORMAT(shipping_fee, 2 decimal places)
    # END IF

#7. Calculate Total Payable
    # SET total_payable TO cost_coffee + sales_tax + shipping fee
    # DISPLAY "Total_payable: $" +FORMAT(total_payable, 2 decimal places)

# END
    

def main():
    PRICE_OVER_40 = 7.50 # Price for over 40lb
    PRICE_OVER_20 = 8.75 # Proce for over 20lb
    PRICE_OVER_10 = 10.00 # Price for over 10lb
    PRICE_ONE_TO_NINE = 12.00 # Price for 1 to 9 pounds


    SALES_TAX_RATE = 0.07 # 7% Sales tax rate
    SHIPPING_RATE_PER_POUND = 1.00 # Shipping tax

    # Get quanity of pounds from customer
    pounds = int(input('How many pounds would'
                       'you like to order? '))
    

    price_per_pound = 0.0

    # Determine the correct price per pound based on weight. 
    if pounds > 40:
        price_per_pound = PRICE_OVER_40
    elif pounds > 20: # This means 21 to 40
        price_per_pound = PRICE_OVER_20
    elif pounds > 9:# This means 10 to 20
        price_per_pound = PRICE_OVER_10
    else: # This means 1 to 9
        price_per_pound = PRICE_ONE_TO_NINE

    # Calculate base cost of the coffee
    cost_coffee = pounds * price_per_pound
    print(f'Your cost of coffee is ${cost_coffee:,.2f}')
    
    
        
    # Determine sales tax
    sales_tax = cost_coffee * SALES_TAX_RATE
    print(f'7% sales tax: ${sales_tax:,.2f}')

    # Calculate shipping
    shipping_fee = 0.00 # Initialize shipping fee

    # Determine shipping fee: free if cost is over $150, ELSE $1 per pound
    if cost_coffee > 150:
        shipping_fee = 0.00
        print(f'Shipping fee: ${shipping_fee:,.2f} (Free shipping!)')
    else:
        shipping_fee = SHIPPING_RATE_PER_POUND * pounds
        print(f'Shipping: ${shipping_fee:,.2f}')
         

    # Display total cost
    total_payable = cost_coffee + sales_tax + shipping_fee
    print(f'Total payable: ${total_payable:,.2f}')

main()

        
    


    
