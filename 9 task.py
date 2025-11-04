word_count = {}
while True:
  line = input('Enter line: ')
  if not line:
    break
  words = line.split()
  for word in words:
    if word in word_count:
      word_count[word] += 1
    else:
      word_count[word] = 1
for word in sorted(word_count):
  print(f"{word} {word_count[word]}")
