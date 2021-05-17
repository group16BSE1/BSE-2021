def counter(s, l):
  word = str(s)
  valueToCheck = str(l)
  count = 0

  for letter in word: 
    if letter == valueToCheck :
      count += 1
  print(f'{letter} = {count}')


counter ('banana', 'a')

counter ('payal', 'p')
