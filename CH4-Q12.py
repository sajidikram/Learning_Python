item=input("What item you want to purchase : ")
item_cost=float(input("Enter the item's cost : "))
saved_cost=float(input("Enter how much you alread saved: "))

balance = item_cost-saved_cost
if (balance<0):
	print("Looks like you already saved enough!")
	balance = 0
	payment = 1
else:
	freq=input("How often Weekly/Monthly/Yearly.... you want to save : ")
	payment = float(input("Enter how much you will save each period: "))
	if (payment <= 0):
		payment = float(input("Savings must be positive. Please enter a positive value:"))

#Calculate number of payments that will be needed

num_remaining_payments = balance/payment

#Present information to user

print("You must make", int(num_remaining_payments), freq, "more payments to buy a "+item)
