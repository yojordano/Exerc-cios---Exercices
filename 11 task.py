line = input('Line: ')
words = line.split()
lower_line = line.lower()
small_words = lower_line.split()

if 'ROBOT' in words:
  print('There is a big robot in the line.')

elif 'robot' in words:
  print('There is a small robot in the line.')

elif 'robot' in small_words:
  print('There is a medium sized robot in the line.')
  
else:
  print('No robots here.')
