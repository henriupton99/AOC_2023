import argparse
import numpy as np

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.m = np.array([list(line) for line in self.file.splitlines()])
    
  def part1(self):
    sum_visible = 2*(len(self.m) + len(self.m[0])) - 4
    for i in range(1,len(self.m)-1):
      for j in range(1,len(self.m[0])-1):
        for section in [self.m[:i,j],self.m[i+1:,j],self.m[i,:j],self.m[i,j+1:]]:
          if max(section) < self.m[i,j]:
            sum_visible += 1
    return sum_visible
  
  def part2(self):
    scenic_scores = []
    for i in range(1,len(self.m)-1):
      for j in range(1,len(self.m[0])-1):
        scenic_score = 1
        for section in [reversed(self.m[:i,j]), self.m[i+1:,j], reversed(self.m[i,:j]), self.m[i,j+1:]]:
          score = 0
          for tree in section:
            if tree >= self.m[i,j]:
              score += 1
              break
            score += 1
          scenic_score *= score
        scenic_scores.append(scenic_score)
    return max(scenic_scores)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
