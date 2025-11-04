start = int(input("Enter the smaller number: "))
end = int(input("Enter the larger number: "))

total = 0

for i in range(start, end + 1):
    total += i ** 2

print(total)
