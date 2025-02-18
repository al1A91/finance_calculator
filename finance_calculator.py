import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n")

# Loop until a valid selection is made
while True:
    selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

    # Investment calculation
    if selection == "investment":
        P = float(input("Enter the amount of money that will be deposited: "))
        r = float(input("Enter the annual interest rate (in %): "))
        t = int(input("Enter the number of years you plan to invest: "))

        # Loop until a valid interest type is chosen
        while True:
            interest = input("Select 'simple' or 'compound' interest: ").lower()

            if interest == "simple":
                A = P * (1 + (r / 100) * t)
                print(f"Your total amount will be: £{round(A, 2)} after {t} years of investment.")
                break
            elif interest == "compound":
                A = P * math.pow((1 + (r / 100)), t)
                print(f"Your total amount will be: £{round(A, 2)} after {t} years of investment.")
                break
            else:
                print("Invalid interest type. Please enter 'simple' or 'compound'.")

        break  # Exit after a valid investment calculation

    # Bond repayment calculation
    elif selection == "bond":
        P = float(input("Enter the present value of the house: "))
        r = float(input("Enter the annual interest rate (in %): "))
        n = int(input("Enter the number of months over which the bond will be repaid: "))

        i = (r / 100) / 12  # Monthly interest rate
        repayment = (i * P) / (1 - (1 + i) ** -n)

        print(f"Your monthly repayment will be: £{round(repayment, 2)} for the next {n} months.")

        break  # Exit after a valid bond calculation

    else:
        print("Invalid entry, please try again.")
