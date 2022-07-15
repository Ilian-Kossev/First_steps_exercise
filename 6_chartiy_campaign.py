number_of_campaign_days = int(input())
number_of_cooks = int(input())
number_of_cakes = int(input())
number_of_gofrettes = int(input())
number_of_pancakes = int(input())
number_of_pancakes_daily = number_of_cooks * number_of_pancakes
sum_of_pancakes_daily = number_of_pancakes_daily * 3.2
number_of_cakes_daily = number_of_cooks * number_of_cakes
sum_of_cakes_daily = number_of_cakes_daily * 45
number_of_gofrettes_daily = number_of_cooks * number_of_gofrettes
sum_of_gofrettes_daily = number_of_gofrettes_daily * 5.8
accumulated_sum_before_expenditures = number_of_campaign_days * (sum_of_gofrettes_daily + sum_of_cakes_daily + sum_of_pancakes_daily)
expenditures = accumulated_sum_before_expenditures / 8
final_accumulated_sum = accumulated_sum_before_expenditures - expenditures
print(final_accumulated_sum)