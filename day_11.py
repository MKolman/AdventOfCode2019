import intcode
from collections import defaultdict

def get_inp():
  with open('input/day_11.txt') as f:
    return list(map(int, f.read().split(',')))

def move(pos, fac):
  if fac == 0: # up
    return pos[0], pos[1]-1
  elif fac == 1: # right
    return pos[0]+1, pos[1]
  elif fac == 2: # right
    return pos[0], pos[1]+1
  elif fac == 3: # left
    return pos[0]-1, pos[1]

def easy():
  state = get_inp()
  pos = (0, 0)
  fac = 0 # up
  colors = defaultdict(int)
  prog = intcode.Runner(state, [0])
  for color in prog:
    colors[pos] = color
    fac += next(prog)*2 - 1
    fac %= 4
    pos = move(pos, fac)
    prog.stdin.append(colors[pos])
  return len(colors)

def hard(debug=False):
  state = get_inp()
  pos = (0, 0)
  fac = 0 # up
  colors = defaultdict(int)
  colors[pos] = 1
  prog = intcode.Runner(state, [1])
  for color in prog:
    colors[pos] = color
    fac += next(prog)*2 - 1
    fac %= 4
    pos = move(pos, fac)
    prog.stdin.append(colors[pos])
  result = '\n'
  xs, ys = zip(*list(colors))
  for y in range(min(ys), max(ys)+1):
    for x in range(min(xs), max(xs)+1):
      result += ' #'[colors[(x, y)]]
    result += '\n'
  return result

def test():
  return easy() == 2018, hard() == '''
  ##  ###  #### #  # ###  #  # ###  ###    
 #  # #  # #    # #  #  # # #  #  # #  #   
 #  # #  # ###  ##   #  # ##   ###  #  #   
 #### ###  #    # #  ###  # #  #  # ###    
 #  # #    #    # #  # #  # #  #  # # #    
 #  # #    #    #  # #  # #  # ###  #  #   
'''

if __name__ == '__main__':
  print(easy())
  print(hard(), 'APFKRKBR')