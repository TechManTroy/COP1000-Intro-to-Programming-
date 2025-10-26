# Troy Edmonds
# 2576081
# COP1000
# Colaborations: none 


# This projects is to demonstrates accuratly calculating the tax,
# tip, and total meal at a resturaunt

#START

# 1. CREATE enviroment by defining MAIN body.
# 2. CREATE input variable name meal_cost for customers to INPUT price.
# 3. CONVERT to FLOAT so we can work with currency.
# 4. CREATE variable for tip named tip_percent 
# 5. CONVERT input to FLOAT 
# 6. CREATE CONSTANT variable for sales tax named SALES_TAX (sales tax is 7)
# 7. DIVIDE tip_percent BY 100
# 8. DIVIDE sales_tax BY 100 
# 7. CALCULATE dollar amount for tip by MULTIPLYING meal_cost price BY tip_rate
# 8. CALCULATE dollar amount of tax by MULTIPLYING meal_cost BY tax_rate
# 9. CALCULATE total_cost by ADDING meal_cost, tip_dollar, and tax_dollar
# 10. DISPLAY the results meal cost, tip dollar, and total cost should show as decimal
#     tip percent and sales tax should show as whole number. 

#END

def main():
    meal_cost = float(input('What is the total cost of your meal? ')) #Input meal price
    tip_percent = float(input('What is the tip percentage ')) #Input tip
    SALES_TAX = 7 #Sales tax CONSTANT

#Convert percentages to thier decial equivalents for calculation. 
    tip_rate = tip_percent / 100
    tax_rate = SALES_TAX / 100

#Calculate dollar amount by MULTIPLYING meal_cost BY tip_rate.
    tip_dollar = meal_cost * tip_rate

#Calculate dollar amount by MULTIPLYING meal_cost BY tax_rate.
    tax_dollar = meal_cost * tax_rate

#Calculate total meal cost by ADDING meal_cost, tip_dollar, and tax_dollar. 
    total_cost = meal_cost + tip_dollar + tax_dollar

#Display results 
    print(f'A ${meal_cost:,.2f} meal with a {tip_percent:.0f}% tip of ${tip_dollar:,.2f} \
and {SALES_TAX:.0f}% tax has a grand total of ${total_cost:,.2f}')

main()
    
    
 

   
   
          
    
    
    
