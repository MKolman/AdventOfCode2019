from collections import defaultdict

def get_inp():
  with open('input/day_06.txt') as f:
    is_orbiting = dict()
    orbiting_me = defaultdict(list)
    for line in f:
      a, b = line.strip().split(')')
      is_orbiting[b] = a
      orbiting_me[a].append(b)
    return is_orbiting, orbiting_me

def easy(orbiting_me, current='COM', path_len=0):
  result = 0
  for planet in orbiting_me[current]:
    result += path_len + 1 + easy(orbiting_me, planet, path_len+1)
  return result

def hard(is_orbiting, orbiting_me, current='YOU', dest='SAN', prev=None):
  if current == dest:
    return 0
  result = -1
  planets = orbiting_me[current]
  if current in is_orbiting:
    planets.append(is_orbiting[current])
  for planet in  planets:
    if planet != prev:
      result = max(result, hard(is_orbiting, orbiting_me, planet, dest, current))
  return result + (result != -1)

def test():
  return easy(get_inp()[1]) == 150150, hard(*get_inp())-2 == 352

if __name__ == "__main__":
  print(easy(get_inp()[1]))
  print(hard(*get_inp())-2)