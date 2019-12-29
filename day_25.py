import intcode
import sys
import curses
from collections import deque
from itertools import product

def get_inp():
  with open('input/day_25.txt') as f:
    return list(map(int, f.read().split(',')))

class Game(object):
  def __init__(self, state):
    self.runner = intcode.Runner(state)
    self.load_room()
    self.pos = 0, 0
    self.visited = set([self.pos])
    self.screen = None

  def show(self):
    if self.screen is None:
      self.screen = curses.initscr()
    self.screen.clear()
    self.screen.addstr(0, 0, self.room_name, curses.A_BOLD)
    self.screen.addstr(1, 0, self.description)
    for i, door in enumerate(self.doors):
      self.screen.addstr(3+i, 0, door)
    for i, item in enumerate(self.items):
      self.screen.addstr(3+i, 10, '{}. {}'.format(i+1, item))

    xs, ys = zip(*self.visited)
    for x in range(min(xs), max(xs)+1):
      for y in range(min(ys), max(ys)+1):
        row, col = y - min(ys) + 3, x - min(xs)+30
        char = 'x' if (x, y) == self.pos else '.#'[(x, y) in self.visited]
        self.screen.addch(row, col, char)
    self.screen.refresh()

  def load_room(self):
    output = ''
    try:
      while not output.endswith('Command?'):
        output += chr(next(self.runner))
    except StopIteration:
      return output

    self.items = self.extract(output, 'Items here:')
    self.doors = self.extract(output, 'Doors here lead:')
    self.room_name = output.split('==')[1]
    self.description = output.split('==\n')[1].split('\n')[0]
    return output

  def take(self, item):
    assert item in self.items, (item, self.items)
    self.runner.stdin += list(map(ord, 'take {}\n'.format(item)))
    output = ''
    while not output.endswith('Command?'):
      output += chr(next(self.runner))
    return output

  def drop(self, item):
    self.runner.stdin += list(map(ord, 'drop {}\n'.format(item)))
    output = ''
    while not output.endswith('Command?'):
      output += chr(next(self.runner))
    return output

  def inv(self):
    self.runner.stdin += list(map(ord, 'inv\n'))
    output = ''
    while not output.endswith('Command?'):
      output += chr(next(self.runner))
    return self.extract(output, 'Items in your inventory:')

  def move(self, door):
    assert door in self.doors, (door, self.doors)
    self.runner.stdin += list(map(ord, door+'\n'))
    self.pos = self.move_pos(self.pos, door)
    self.visited.add(self.pos)
    return self.load_room()

  def play(self):
    while True:
      self.show()
      char = self.screen.getch()
      if char == 113: break  # q
      elif char == ord('d'): self.move('east')
      elif char == ord('a'): self.move('west')
      elif char == ord('w'): self.move('north')
      elif char == ord('s'): self.move('south')

  def __str__(self):
    return '{}\n{}\n{}\n'.format(self.room_name, self.items, self.doors)

  def extract(self, txt, prompt):
    if prompt not in txt:
      return []
    lines = txt.split(prompt)[-1].split('\n')
    items = []
    for line in lines[1:]:
      if not line.startswith('- '):
        break
      items.append(line[2:])
    return items

  def move_pos(self, pos, door):
    dpos = {
      'north': (0, -1),
      'south': (0, 1),
      'west': (-1, 0),
      'east': (1, 0)
    }
    return pos[0]+dpos[door][0], pos[1]+dpos[door][1]

def back(door):
  return {
    'north': 'south',
    'south': 'north',
    'east': 'west',
    'west': 'east',
  }[door]
forbidden = ['photons', 'molten lava', 'infinite loop', 'escape pod', 'giant electromagnet']

def dfs(game, prev=None):
  # print(game.room_name)
  if game.room_name == ' Security Checkpoint ':
    return game.inv()
  for item in game.items:
    if item not in forbidden:
      # print('    Taking', item)
      game.take(item)
  for door in game.doors[::-1]:
    if door != prev:
      game.move(door)
      inv = dfs(game, back(door))
      if inv:
        return inv
      game.move(back(door))

class Queue(object):
  def __init__(self, start=None):
    self.data = start or []
  def __len__(self):
    return 1
  def __getitem__(self, key):
    if isinstance(key, slice):
      return self
    if not self.data:
      self.data += list(map(ord, input('Type: ') + '\n'))

    result, self.data = self.data[0], self.data[1:]
    return result

def find_weight(game):
  inv = game.inv()
  state = [1 for _ in inv]
  for new_state in product([1, 0], repeat=len(inv)):
    # print(','.join(item for i, item in zip(new_state, inv) if i))
    for old, new, item in zip(state, new_state, inv):
      if new == old:
        continue
      if new:
        game.take(item)
      else:
        game.drop(item)
    state = new_state
    output = game.move('south')
    if 'Security Checkpoint' not in output:
      for word in output.split():
        if word.isdigit():
          return word

def manual(runner):
  runner = runner or intcode.Runner(get_inp())
  runner.stdin = Queue()
  for c in runner:
    print(chr(c), end='')
    sys.stdout.flush()

def easy():
  game = Game(get_inp())
  dfs(game)
  return find_weight(game)
  manual(game.runner)

def hard():
  pass

def test():
  return easy() == '33624080', hard() == None

if __name__ == '__main__':
  print(easy())
