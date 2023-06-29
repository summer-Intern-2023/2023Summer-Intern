def part_a(annual_salary, portion_saved, total_cost):
    
    portion_down_payment = 0.25
    r = 0.04
    current_savings = 0.0
    count_month = 0

    down_payment_amount = total_cost * portion_down_payment
    monthly_salary = (annual_salary / 12) * portion_saved
    monthly_r = r / 12

    while current_savings < down_payment_amount:
        monthly_investment = current_savings * monthly_r
        current_savings = monthly_salary + current_savings + monthly_investment
        count_month += 1

    print("Number of months:", count_month)
    return count_month