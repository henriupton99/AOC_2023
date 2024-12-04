import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()

    self.sections = []
    for line in self.lines:
      ranges = []
      for section in line.split(','):
        lb, ub = map(int, section.split('-'))
        range_set = set(range(lb,ub+1))
        ranges.append(range_set)
      self.sections.append(ranges)

    
  def part1(self):
    is_inclued = 0
    for section in self.sections:
      if section[0].difference(section[1]) == set() or section[1].difference(section[0]) == set() :
        is_inclued += 1
    return is_inclued
  
  def part2(self):
    have_intersection = 0
    for section in self.sections:
      if section[0].intersection(section[1]) != set():
        have_intersection += 1
    return have_intersection
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
