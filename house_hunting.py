# Write your code here
total_cost = input("What is the price of your dream home?")
portion_down_payment = 0.25
print(total_cost)
current_savings = 0

i = 0
#when i use i=0 test 1 is off by one month and test 2 is correct
#when i use i=1 test 1 is corect and test 2 is off by one month

while current_savings < portion_down_payment:
    current_savings += monthly_salary_saved
    investment_return += current_savings * (.04/12)
    current_saving += investment_return
    i+=1

print("Number of Months", i)
# print ("you will have enough money in", i, "months for a down payment on your new home!")