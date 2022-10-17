# class income
name = input("What is your name? ")
print(f"Hello their {name}, We are going to calculate your ROI looking at multiple rental income. ")


monthly = int(input('What is your rental monthly income? '))
#monthly is the 2nd asked question right here as we continue to ask for

side_hussle = int(input("How much is your total side income in a month? "))
# add up up side_hussle1 and add up the monthly income 


#calulate total monthly support

total = monthly + side_hussle

print("-" *40)
print("Your Total monthly income is $" + str(total))

print("-" *40)
# class Expense:
#EXPESNES
# def spending(self):
print("Lets calculate your total Monthly expenses.")

first_expense = int(input("How much is the taxes on the propety? "))

insurance = int(input('What is the cost of insurance in a month? '))

utilities = int(input("What is the monthly total utility fees? "))

maintaning = int(input("How much is the total repairs of the property? "))

mortgage = int(input("What is your Mortgage expense? "))

#add up total monthly expenses
total1 = first_expense + insurance + utilities + maintaning + mortgage

print("Your total Monthly expenses are $" + str(total1))

print("-" *40)


#subtract total from your income to your total monthly expenses

important = total - total1

print("The total cash flow in a month is $" + str(important))

print("-" *40)


#class Investments()
print("Let's look at your Invesments")

down_payment = int(input("What is your down payment? "))

closing_cost = int(input("What was your closing cost? "))

rehab = int(input("What was your rehab budget? "))


total2 = down_payment + closing_cost + rehab

print("-" *40)
print("Your total investments are $" + str(total2))

print("-" *40)

print("Total Monthly income is $" + str(total))
print("Total Monthly Expenses are $" + str(total1))
print("Total investments are $" + str(total2))


#return the RIO percentage

total3 = total / total1 / total2
print("Your cash on cash ROI is %" + str(total3))