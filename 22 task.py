cars_input = input("Cars: ")

cars = cars_input.split()

red_count = cars.count("red")
blue_count = cars.count("blue")

print(f"red: {red_count}")
print(f"blue: {blue_count}")
