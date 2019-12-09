import intcode

def get_inp():
  with open('input/day_09.txt') as f:
    return list(map(int, f.read().split(',')))

def easy():
  return next(intcode.Runner(get_inp(), [1]))

def hard():
  return next(intcode.Runner(get_inp(), [2]))

def test():
  return easy() == 2752191671, hard() == 87571

if __name__ == '__main__':
  print(easy())
  print(hard())