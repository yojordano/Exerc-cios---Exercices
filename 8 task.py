car_count= {}
while True:
  color = input('Car: ')
  if color == "":
    break
  if color in car_count:
    car_count[color] += 1 
  else:
    car_count[color] = 1
for color, count in car_count.items():
  print(f"Cars that are {color}: {count}")
