deposit_sum = float(input())
deposit_period = int(input())
annual_interest_rate = float(input())
monthly_interest = deposit_sum * annual_interest_rate / 100 / 12
final_sum = deposit_sum + deposit_period * monthly_interest
print(final_sum)
