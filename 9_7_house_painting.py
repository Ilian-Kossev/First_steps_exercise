x_house_height = float(input())
y_house_length = float(input())
h_house_roof_height = float(input())
window_area = 1.5 * 1.5 * 2
door_area = 1.2 * 2
front_and_rear_wall_area = x_house_height * x_house_height * 2 - door_area
side_wall_area = y_house_length * x_house_height * 2 - window_area
front_and_rear_roof_area = (x_house_height * h_house_roof_height / 2) * 2
side_roof_area = y_house_length * x_house_height * 2
needed_litres_green_paint = (front_and_rear_wall_area + side_wall_area) / 3.4
needed_litres_red_paint = (front_and_rear_roof_area + side_roof_area) / 4.3
print(f"{needed_litres_green_paint:.2f}")
print(f"{needed_litres_red_paint:.2f}")
