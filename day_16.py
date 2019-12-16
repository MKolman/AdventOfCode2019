
def get_inp():
  with open('input/day_16.txt') as f:
    return list(map(int, f.read().strip()))

def convo(inp, n):
  pattern = 0, 1, 0, -1
  result = 0
  for i in range(n-1, len(inp), 4*n):
    result += sum(inp[i:i+n])
    result -= sum(inp[i+2*n:i+3*n])
  return abs(result) % 10

def easy():
  inp = get_inp()
  for i in range(100):
    inp = [convo(inp, j+1) for j in range(len(inp))]
  return ''.join(map(str, inp[:8]))

def hard():
  inp = get_inp()
  inp *= 10000
  offset = int(''.join(map(str, inp[:7])))
  inp = inp[offset:]
  for i in range(100):
    new_inp = [0] * len(inp)
    new_inp[-1] = inp[-1]
    for j in range(len(inp)-2, -1, -1):
      new_inp[j] = (new_inp[j+1] + inp[j]) % 10
    inp = new_inp
  return ''.join(map(str, inp[:8]))

def test():
  return easy() == '90744714', hard() == '82994322'

if __name__ == '__main__':
  print(easy())
  print(hard())
