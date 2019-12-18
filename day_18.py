from collections import deque
import heapq
from string import ascii_lowercase

def get_inp():
  with open('input/day_18.txt') as f:
    return [line.strip() for line in f]

def get_nei(x, y):
  for d in [-1, 1]:
    yield x + d, y
    yield x, y + d

def flood(inp, startpos):
  visited = set([startpos])
  result = dict()
  q = deque([(0, startpos, set())])
  while q:
    dist, pos, keys = q.popleft()
    for x, y in get_nei(*pos):
      cell = inp[y][x]
      if cell == '#' or (x, y) in visited:
        continue
      visited.add((x, y))
      if cell.islower():
        result[cell] = dist+1, keys
        continue 
      new_keys = set(keys)
      if cell.isupper():
        new_keys.add(cell.lower())
      q.append((dist+1, (x, y), new_keys))
  return result

def get_pos(inp, char):
  return [(x, y) for y, line in enumerate(inp) for x, c in enumerate(line) if c == char]

def get_graph(inp):
  graph = dict()
  poss = dict()
  for c in ascii_lowercase + '@':
    pos = get_pos(inp, c)
    if len(pos) == 1:
      poss[c] = pos[0]
      graph[c] = flood(inp, pos[0])
    elif len(pos) > 1:
      for i, p in enumerate(pos):
        poss[c+str(i)] = p
        graph[c+str(i)] = flood(inp, p)
  return graph, poss

def dijkstra(graph):
  start = tuple(k for k in graph if '@' in k)
  visited = set([(start, frozenset(start))])
  q = [(0, list(start), frozenset(start))]
  while q:
    dist, current_list, keys = heapq.heappop(q)
    for i, current in enumerate(current_list):
      for nei, (cost, key_cost) in graph[current].items():
        nei_list = current_list[:]
        nei_list[i] = nei
        cache_key = tuple(nei_list), keys
        if not key_cost <= keys or cache_key in visited:
          continue
        visited.add(cache_key)
        new_keys = keys.union(nei)
        if len(new_keys) == len(graph):
          return dist + cost
        heapq.heappush(q, (dist+cost, nei_list, new_keys))

def swap(inp):
  inp = [list(line) for line in inp]
  x, y = get_pos(inp, '@')[0]
  for i in range(-1, 2):
    for j in range(-1, 2):
      inp[y+i][x+j] = '#@'[abs(i) + abs(j) == 2]
  inp = [''.join(line) for line in inp]
  return inp

def easy():
  return "FIXME"
  inp = get_inp()
  graph, pos = get_graph(inp)
  return dijkstra(graph)

def hard():
  return "FIXME"
  inp = get_inp()
  inp = swap(inp)
  graph, pos = get_graph(inp)
  return dijkstra(graph)

def test():
  return easy() == 4228, hard() == 1858

if __name__ == '__main__':
  print(easy())
  print(hard())