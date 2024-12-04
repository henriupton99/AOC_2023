import argparse
from itertools import product

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.matrix = [list(line) for line in self.file.splitlines()]
    self.nrows, self.ncols = len(self.matrix), len(self.matrix[0])
    
    self.matches = 0
    
  def part1(self):
    word_to_find = 'XMAS'
    for i in range(len(self.matrix)):
      for j in range(len(self.matrix[0])):
        if self.matrix[i][j] == 'X':
          for di, dj in list(product([-1,0,1],[-1,0,1])):
            if di == dj ==0:
              continue
            if all(0 <= i + k*di < self.nrows and 0 <= j + k*dj < self.ncols and 
                  self.matrix[i + k*di][j + k*dj] == word_to_find[k]
                  for k in range(len(word_to_find))):
              self.matches += 1
    return self.matches
  
  def part2(self):
    for i in range(1,self.nrows-1):
      for j in range(1,self.ncols-1): 
        if self.matrix[i][j] == 'A':
          first_bar = self.matrix[i-1][j-1] + self.matrix[i][j] + self.matrix[i+1][j+1]
          second_bar = self.matrix[i-1][j+1] + self.matrix[i][j] + self.matrix[i+1][j-1]
          if first_bar in ['SAM','MAS'] and second_bar in ['MAS','SAM']:
            self.matches += 1
    return self.matches
        
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
