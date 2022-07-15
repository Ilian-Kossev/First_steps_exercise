length = int(input())
width = int(input())
height = int(input())
occupied_volume_percent = float(input())
total_volume = length * width * height / 1000
real_volume = total_volume - total_volume * occupied_volume_percent / 100
print(real_volume)
# alt:
#length = int(input())
#width = int(input())
#height = int(input())
#occupied_volume_percent = float(input())
#total_volume = length * width * height
#total_volume *= 1 - occupied_volume_percent / 100
#real_volume = total_volume * 0.001
#print(real_volume)