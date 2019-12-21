import intcode
from collections import deque

def get_inp():
  with open('input/day_21.txt') as f:
    return list(map(int, f.read().split(',')))

def easy():
  state = get_inp()
  # J = (!A OR !B OR !C) AND D
  stdin = '''
NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
'''.strip() + '\n'
  runner = intcode.Runner(state, list(map(ord, stdin)))
  return list(runner)[-1]

def hard():
  state = get_inp()
  # J = (!A OR !B OR !C) AND D AND (E OR H)
  stdin = '''
NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT D T
OR E T
OR H T
AND T J
RUN
'''.strip() + '\n'
  runner = intcode.Runner(state, list(map(ord, stdin)))
  return list(runner)[-1]

def test():
  return easy() == 19352638, hard() == 1141251258

if __name__ == '__main__':
  print(easy())
  print(hard())