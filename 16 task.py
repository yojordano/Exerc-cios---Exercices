all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

rainy_days_input = input("Which days had rain? ")

if rainy_days_input.strip() == "":
    rainy_days = []
else:
    rainy_days = rainy_days_input.split()

rain_free_days = len(all_days) - len(rainy_days)

print(f"Number of days without rain: {rain_free_days}")




#Which days had rain? Monday Tuesday Wednesday Number of days without rain: 4
