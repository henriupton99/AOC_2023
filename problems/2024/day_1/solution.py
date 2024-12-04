import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = [l.split('  ') for l in self.file.splitlines()]
    self.list1 = sorted([int(l[0]) for l in self.lines])
    self.list2 = sorted([int(l[1]) for l in self.lines])
    
  def part1(self):
    return sum(abs(l-r) for l,r in zip(self.list1,self.list2))
  
  def part2(self):
    similarity_score = 0
    for num_l in self.list1:
      nb_occurs_r = len([num_r for num_r in self.list2 if num_r == num_l])
      similarity_score += num_l * nb_occurs_r
    return similarity_score
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
