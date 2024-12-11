import argparse
import functools

@functools.cache
def nb_stones_after_n_blinks(stone, n):
  if n == 0:
    return 1
  if stone == 0:
    result = nb_stones_after_n_blinks(1, n-1)
  elif len(str(stone)) % 2 == 0:
    stone = str(stone)
    result = 0
    result += nb_stones_after_n_blinks(int(stone[:len(stone)//2]), n-1)
    result += nb_stones_after_n_blinks(int(stone[len(stone)//2:]), n-1)
  else:
    result = nb_stones_after_n_blinks(2024 * stone, n-1)
  return result
  
class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'

  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.stones = list(map(int, [line.split() for line in self.file.splitlines()][0]))
    self.n_stones = 0
    
  def part1(self):
    for stone in self.stones:
      self.n_stones += nb_stones_after_n_blinks(stone, 25)
    return self.n_stones
  
  def part2(self):
    for stone in self.stones:
      self.n_stones += nb_stones_after_n_blinks(stone, 75)
    return self.n_stones
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
