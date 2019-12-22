from sys import version_info

def get_inp():
  with open('input/day_22.txt') as f:
    for line in f:
      if 'stack' in line:
        yield 'reverse', 0
      else:
        sp = line.split()
        yield sp[0], int(sp[-1])

def easy():
  inp = get_inp()
  current_position, N = 2019, 10007
  for command, num in inp:
    if command == 'reverse':
      current_position = N - current_position - 1
    elif command == 'cut':
      num %= N
      if current_position >= num:
        current_position -= num
      else:
        current_position += N-num
    elif command == 'deal':
      current_position = (current_position * num) % N
  return current_position


def reverse_shuffle(inp, a, m, N):
  command, num = inp.pop()
  if len(inp):
    a, m = reverse_shuffle(inp, a, m, N)

  if command == 'reverse':
    m *= -1
    a += m
  elif command == 'cut':
    a += num * m
  elif command == 'deal':
    m *= pow(num, -1, N)

  return a, m

def hard(N=119315717514047, times=101741582076661, pos=2020):
    if (version_info.major, version_info.minor) < (3, 8):
      # Python 3.8 needed for modular inverse,
      # because I was too lazy to write it myself
      return None

    a, m = reverse_shuffle(list(get_inp()), 0, 1, N)
    a = a * (1 - pow(m, times, N)) * pow(1 - m, -1, N)
    m = pow(m, times, N)

    return (pos * m + a) % N


def test():
  return easy() == 7171, hard() == 73394009116480

if __name__ == '__main__':
  print(easy())
  print(hard())
