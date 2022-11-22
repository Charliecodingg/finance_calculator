#This program is a set of two financial calculators, one to calculate investments and one to calculate bonds.

#The user selects the calculator they need, then input the appropriate information to fill out the formulae.

#The program calculates the answers using the users information, then displays an output appropriately.

import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")

print("\ninvestment - to calculate the amount of interest you'll earn on your investment.")

print("bond  -   to calculate the amount you'll have to pay on a home loan.")

menu_selection = input("Please enter your selection: ")

#Here the program splits into the investment and bond sections. Using several or logical operators to allow for various entries without error.

#I had some issues getting the if statement to work correctly. after looking up the issue i discovered that or statements need to be formatted in the below manner.
# the website that provided this information was https://stackoverflow.com/questions/11780957/python-function-runs-to-first-if-statement-no-matter-input

# several \n have been added to improve readability for the user
if menu_selection == "investment" or menu_selection == "Investment" or menu_selection == "INVESTMENT":

    invest_amount = int(input("\nPlease enter the amount of money you will deposit: "))

    interest_rate = int(input("\nPlease enter the interest rate: "))

    invest_length = int(input("\nPlease enter the amount of years you wish to invest: "))

    print("\nWhich type of interest do you wish to use?")

    print("\nSimple ")

    print("Compound ")

    invest_type = input("\nPlease enter your selection: ")

    #The program then splits again into the simple and compound methods of interest. Using several acceptable answers and a failsafe else to improve usability 
    
    if invest_type == "simple" or invest_type == "SIMPLE" or invest_type == "Simple":

        interest_rate = interest_rate/100

        total_amount = invest_amount * (1 + interest_rate * invest_length)
        
        total_amount = round(total_amount,2)
        
        print(f"\nThe amount you will receive after {invest_length} years is £{total_amount}. Your original investment was £{invest_amount} ")
    
    elif invest_type == "compound" or invest_type == "COMPOUND" or invest_type == "Compound":       

        interest_rate = interest_rate/100

        total_amount = invest_amount*(math.pow((1+interest_rate), invest_length))
        
        total_amount = round(total_amount,2)
        
        print(f"\nThe amount you will receive after {invest_length} years is £{total_amount}. Your original investment was £{invest_amount} ")
    
    else:
        print("Please enter a valid selection")


elif menu_selection == "bond" or menu_selection == "BOND" or menu_selection == "Bond":
    
    house_value = int(input("\nPlease enter the value of your house: "))

    interest_rate = int(input("\nPlease enter the interest rate: "))
    
    bond_length = int(input("\nPlease enter the amount of months you plan to repay the bond in: "))
    
    interest_rate = interest_rate/100

    interest_rate = interest_rate/12

    monthly_repayment =  (interest_rate*house_value)/(1-(1+interest_rate)**(-bond_length))
    
    monthly_repayment = round(monthly_repayment,2)
    
    #here the program excecutes the formula based on the users inputs and displays it to two decimal places as it is currency
    
    print(f"\nThe amount you will need to repay monthly is £{monthly_repayment}")

else:
    print("Please make a valid selection")
