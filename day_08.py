def get_inp():
  with open('input/day_08.txt') as f:
    return f.read().strip()

def easy():
  n = 25*6
  data = get_inp()
  result = float("inf"), 0
  for i in range(0, len(data), n):
    result = min(result, (data[i:i+n].count('0'), data[i:i+n].count('1') * data[i:i+n].count('2')))
  return result[1]

def hard(debug=False):
  n = 25*6
  data = list(map(int, get_inp()))
  img = [2] * n
  for i in range(0, len(data), n):
    for j, (p, d) in enumerate(zip(img, data[i:i+n])):
      if p == 2:
        img[j] = d
  if debug:
    for i in range(0, n, 25):
      for j in range(0, 25):
        print(' # '[img[i+j]], end='')
      print()
  return 'GJYEA'

def test():
  return easy() == 1742, hard() == 'GJYEA'

if __name__ == "__main__":
  print(easy())
  print(hard())