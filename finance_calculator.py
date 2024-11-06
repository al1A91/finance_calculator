Data_Engineer
# this is a investment and bond calculator.
 
import math

print("investment - to calculate the amount of interest you'll earn on your investment")

print("bond       - to calculate the amount you'll have to pay on a home loan\n")

# the value below determines selection using Booleans method of True or False.
# the program will continuosly ask the question unless the conditions are met.

while (True):

    # selection stores our input of investment or bond. 
    
    selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # investment
        
    if selection == ("investment"):
        
        P = float(input("Enter the amount of money that will be deposited: "))

        r = float(input("Enter interest rate in percent: "))

        t = int(input("Enter planned years of investment: "))
        
        

        # the output is determined on input simple or compund.
        # break will stop the programe once the conditinos are met.
        
        while (True):
            
            interest = input("Select 'simple' or 'compound' plan: ").lower()

            if interest == "simple":
                
                A = P * (1 + (r*0.01)*t)
                
                print("Your total amoutn will be:",round (A,2),"for",t,"years of investment.")

                break

        
            elif interest == "compound":

                A = P * math.pow((1 + (r*0.01)), t)
                
                print("Your total amount will be:",round (A,2),"for",t,"years of investment.")
                
                break            

            else:
                print("Invalid interest selected.")

        break
            
    
    

    # Bond repayment

    elif selection == ("bond"):   
    
        P = float(input("Enter the present value of the house: "))

        r = float(input("Enter the interest rate: "))

        n = int(input("Enter the number of months over which the bond will be repaid: "))

        i = n/12

        repayment = ((i * 0.01) * P) / (1 - (1 + i)**(-n))

        print("Your repayment is:",round (repayment,2),"per month for the next",n, "months.")

        break

    else:
        print("Invalid entry please try again.")
