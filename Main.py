#Change Calculator
# Read in a cost
# Read in the amount given
# Calculate the change
# Break the change into how many nickels, dimes, quarters
# loonies, toonies, $5s, $10s, $20s, $50s, $100s
# If amount is below the cost, say how much more they owe.
Cost=float(input ("How much does the item cost?"))
amount=float(input("what the payment?"))
change=amount-cost
print("Your change is",change)
num100=change//100
print(num100,"x $100")
change=change&100
num100=change//50
print(num100,"x $50")
change=change&50
