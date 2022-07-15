w = float(input())
h = float(input())
possible_number_of_seats_w = w * 100 // 120
possible_number_of_seats_h = (h * 100 - 100) // 70
total_possible_number_seats = possible_number_of_seats_w * possible_number_of_seats_h
real_number_of_seats = total_possible_number_seats - 3
print(int(real_number_of_seats))
