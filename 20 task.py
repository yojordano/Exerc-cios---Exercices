current_floor = int(input("Current floor: "))
destination_floor = int(input("Destination floor: "))

for floor in range(current_floor, destination_floor + 1):
    print(f"Level {floor}")
