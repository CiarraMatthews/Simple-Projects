#The app without the GUI

def by_net_income():
	#Fix the taxes!
	income = int(input("Please enter your income here: "))
	print("You can afford : $", income * 0.33, "/mo, with a net income of ", income)

def by_gross_income():
	#Fix the loop. Implement try and catch. Implement percentage options
	try:
		income = int(input("Please enter your income here: "))
	except ValueError:
		print("Please enter a valid number")
	try:
		choice = int(input("Press 1 for default rent percentage of 33%, 2 to chose your own percentage "))
	except ValueError:
		print("Please enter a valid number")
	if choice == 1:
		print("You can afford : $", income * 0.33, "/mo")
	elif choice == 2:
		print("You can afford : $", income * percentages(), "/mo")
	else:
		print("Please chose one of the two options presented: ")
		by_gross_income()

def by_hourly():
	#Fix taxes. Take from net when done
	income = int("Please enter your income here: ")


def by_yearly():
	#Check for accuracy
	income = int("Please enter your salary here: ")
	print("You can afford : $", income/12 * 0.33, "/mo")

def percentages():
	try:
		percent = int(input("Please input a value between 10 and 40%: "))
	except ValueError:
		print("Please enter a valid number")
	return percent/100

def find_taxes():
	pass

def main():
	print("Press 1 to calculate by monthly net income \nPress 2 to calculate by monthly gross income \nPress 3 to start calculating by hourly pay \nPress 4 to calculate by yearly pay", end="")
	choice = int(input(": "))
	if choice == 1:
		by_net_income()
	elif choice == 2:
		by_gross_income()
	elif choice == 3:
		by_hourly()
	elif choice == 4:
		by_yearly()
	else:
		print("Wrong choice")

main()

