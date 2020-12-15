#The app without the GUI

def by_net_income():
	income = int(input("Please enter your income here: "))
	print("You can afford :", income * 0.33, "/mo")

def by_gross_income():
	income = int(input("Please enter your income here: "))
	choice = int(input("Press 1 for default rent percentage of 33%, 2 to chose your own percentage"))
	if choice == 1:
		print("You can afford :", income * 0.33, "/mo")
	elif choice == 2:
		print("Okay")
	else:
		print("Please chose one of the two options presented")
		by_gross_income()

def by_hourly():
	pass
	income = int("Please enter your income here")

def by_yearly():
	income = int("Please enter your income here")
	print("You can afford :", income/12 * 0.33, "/mo")


def main():
	print("Press 1 to calculate by monthly net income \nPress 2 to calculate by monthly gross income \nPress 3 to start calculating by hourly pay \nPress 4 to calculate by yearly pay", end="")
	choice = int(input(": "))
	switcher={
		1: by_net_income(),
		2: by_gross_income(),
		3: by_hourly(),
		4: by_yearly()
	}

main()

