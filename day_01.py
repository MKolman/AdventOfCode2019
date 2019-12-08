def get_inp():
  with open('input/day_01.txt') as f:
    for line in f:
      yield int(line)

def easy():
  result = 0
  for inp in get_inp():
    result += inp // 3 - 2
  return result

def hard():
  result = 0
  for inp in get_inp():
    inp = inp // 3 - 2
    while inp > 0:
      result += inp
      inp = inp // 3 - 2
  return result

def test():
  return easy() == 3320226, hard() == 4977473

if __name__ == "__main__":
  print(easy())
  print(hard())
