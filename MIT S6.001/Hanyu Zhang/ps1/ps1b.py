annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(
    input("Enter the Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

r = 0.04
month = 0
portion_down_payment = 0.25
current_savings = 0.0
real_pay = portion_down_payment * total_cost

while current_savings < real_pay :
    investments_earning_monthly = current_savings * r / 12
    current_savings = current_savings + (annual_salary / 12) * portion_saved + investments_earning_monthly
    month += 1
    if month % 6 == 0 :
        annual_salary = annual_salary + semi_annual_raise * annual_salary

print("Number of months: ", month)