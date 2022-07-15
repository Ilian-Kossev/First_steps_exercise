number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
total_reading_hours = number_of_pages / pages_per_hour
necessary_days = total_reading_hours / number_of_days
print(necessary_days)
