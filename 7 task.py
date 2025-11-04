namecolour = {}
namecolour1 = {}

line = input('Name and colour: ')
while line:
  name, colour = line.split()
  namecolour[name] = colour
  namecolour1[name] = name
  line = input('Name and colour: ')

for letter in namecolour:
  print(namecolour1[letter], namecolour[letter])
  print(end='')
