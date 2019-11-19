# Certain function in python become available when yoi import their respective modules
import math

# Only the number of the interest rate should be entered - don’t worry about having to deal with the added ‘%’,
# e.g. The user should enter 8 and not 8%.

P = float(input("Enter the dollar amount you want deposit: ")) # The amount that they are depositing, stored as ‘P’.
i = int(input("Enter your bank interest rate: ")) # The interest rate (as a percentage), stored as ‘i’.
t = int(input("How long do you plan to invest? (enter year): ")) # The number of years of the investment. stored as ‘t’.

# Then ask the user to input whether they want “simple” or “compound” interest, and store this in a variable called ‘interest’.
choice = input("Please choose your plan (simple or compound): ")

r = i/100 # to convert i to a percentage, define the variable r

# Simple interest rate is calculates as follows: simple = P(1 + r * t)
simple = round((P*(1+r*t)) , 2) # The Python equvalent is very similar

# Compound interest rate is calculated as follows: compound = P(! + r) ^ t
compound = round((P*math.pow((1+r),t)) , 2) # The Python equicalent is slightly different

# Depending on whether they typed “simple” or “compound”, output the appropriate amount that they will get after the given period at the interest rate.
# Print out the answer!
if choice == "simple":
    print ("Here is the total: R" , str(simple))
elif choice == "compound":
    print ("Here is the total: R" , str(compound))
