import argparse
from collections import defaultdict

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.rules, self.pages = open(self.filename,'r').read().split('\n\n')
    self.updates = [list(map(int, line.split(','))) for line in self.pages.splitlines()]

    self.orders = defaultdict(list)
    for order in self.rules.splitlines():
      lower, greater = order.split('|')
      self.orders[int(lower)].append(int(greater))
    
    self.score = 0

  def part1(self):
    for pages in self.updates:
      sorted_pages = sorted(pages, key=lambda page: -len([order for order in self.orders[page] if order in pages]))
      if pages == sorted_pages:
        self.score += pages[len(pages) // 2]
    return self.score
  
  def part2(self):
    for pages in self.updates:
      sorted_pages = sorted(pages, key=lambda page: -len([order for order in self.orders[page] if order in pages]))
      if pages != sorted_pages:
        self.score += sorted_pages[len(sorted_pages) // 2]
    return self.score
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
