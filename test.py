import time

def test():
  start = time.time()
  for d in range(1, 26):
    result = 'Day {:2d} '.format(d)
    try:
      t = time.time()
      solution = __import__('day_{:02d}'.format(d))
      e, h = solution.test()
      result += '{} {} ({}s)'.format(' ✓'[e], ' ✓'[h], round(time.time() - t, 3))
    except ModuleNotFoundError:
      result += '✗ ✗'
    print(result)
  print('[Finished in {}s]'.format(round(time.time() - start, 2)))

if __name__ == '__main__':
  test()