#The app without the GUI

def by_net_income():
	print("Net plz")

def by_gross_income():
	income = int("Please enter your income here")
	choice = int("Press 1 for default rent percentage of 33%, 2 to chose your own percentage")
	if choice == 1:
		print("You can afford :", income * 0.33, "/mo")
	elif choice == 2:
		print("Okay")
	else:
		print("Please chose one of the two options presented")
		by_gross_income()

def by_hourly():
	pass

def main():
	print("Press 1 to calculate by monthly net income \nPress 2 to calculate by monthly gross income \nPress 3 to start calculating by hourly pay", end="")
	choice = int(input(": "))
	switcher={
		1: by_net_income(),
		2: by_gross_income(),
		3: by_hourly(),
	}

main()

