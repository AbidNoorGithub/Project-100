class ATM:
	def __init__(self, name, amount):
		self.name = name
		self.amount = amount

	def withdraw(self, amountWithdrawn):
		self.amount -= amountWithdrawn
		print("You now have " + str(self.amount)+ "\n")

	def deposit(self,amountDeposited):
		self.amount += amountDeposited
		print("You now have " + str(self.amount)+ "\n")

	def info(self):
		print(self.name + " Has " + str(self.amount) + "\n")


Abid = ATM("Abid", 200)

Abid.withdraw(100)

Abid.deposit(150)

Abid.info()