bill = float(input("What was the total bill?\n $"))

tip = float(input("What percentage Tip would you like to give?\n %"))

group = int(input("How many people to split the bill?\n "))

share = "{:.2f}".format(bill / group + (bill * ((tip / 100) / group)))

print(f"Each one of you should pay: ${share}")
