import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.grid, self.instructions = self.file.split('\n\n')
    self.instructions = [{">":1,"^":-1j,"<":-1,"v":1j}[c] for c in self.instructions.replace("\n", "")]

  def push(self, i, c, do_it):
    if self.matrix[i+c] == "#": val = False
    elif self.matrix[i+c] == ".": val = True
    elif c.imag==0 or self.matrix[i+c] == "O": val = self.push(i+c, c, do_it)
    elif self.matrix[i+c] == "[": val = self.push(i+c, c, do_it) and self.push(i+1+c, c, do_it)
    elif self.matrix[i+c] == "]": val = self.push(i+c, c, do_it) and self.push(i-1+c, c, do_it)
    if do_it: self.matrix[i+c], self.matrix[i] = self.matrix[i], self.matrix[i+c]
    return val
    
  def part1(self):
    self.matrix = {c+1j*r:v for r,l in enumerate(self.grid.split('\n')) for c,v in enumerate(l.strip())}
    r = next(k for k,v in self.matrix.items() if v=="@")
    for c in self.instructions:
      if self.push(r, c, False):
        self.push(r, c, True)
        r += c
    return int(sum(k.real + 100*k.imag for k,v in self.matrix.items() if v in "[O"))
  
  def part2(self):
    self.grid = self.grid.replace("#","##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    self.matrix = {c+1j*r:v for r,l in enumerate(self.grid.split('\n')) for c,v in enumerate(l.strip())}
    r = next(k for k,v in self.matrix.items() if v=="@")
    for c in self.instructions:
      if self.push(r, c, False):
        self.push(r, c, True)
        r += c
    return int(sum(k.real + 100*k.imag for k,v in self.matrix.items() if v in "[O"))
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
