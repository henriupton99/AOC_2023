import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    self.priorities = {letter : k+1 for (k,letter) in enumerate(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))}
    
  def part1(self):
    self.common_items = []
    self.common_items_points = []
    for line in self.lines:
      split_index = len(line) // 2
      first_bag, second_bag = line[:split_index], line[split_index:]
      items_first_bag, items_second_bag = set(first_bag), set(second_bag)
      common_item = list(items_first_bag.intersection(items_second_bag))[0]
      self.common_items.append(common_item)
      self.common_items_points.append(self.priorities[common_item])
    return sum(self.common_items_points)
  
  def part2(self):
    bags_points = []
    n_bags = len(self.lines) // 3
    for i in range(n_bags):
      bag = self.lines[i*3:(i+1)*3]
      intersection = set(bag[0])
      for b in bag[1:]:
        intersection = intersection.intersection(set(b))
      common_item = list(intersection)[0]
      bag_points = self.priorities[common_item]
      bags_points.append(bag_points)
    return sum(bags_points)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
