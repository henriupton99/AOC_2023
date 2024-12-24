import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))

  def process_gate(self, left: str, right: str, dir: str, instr: str) -> int:
    if instr == 'AND':
      if self.key_values[left] == 1 and self.key_values[right] == 1:
        self.key_values[dir] =  1
      else:
        self.key_values[dir] = 0
    if instr == 'XOR':
      if (self.key_values[left] == 1 and self.key_values[right] == 0) or (self.key_values[left] == 0 and self.key_values[right] == 1):
        print(dir)
        self.key_values[dir] = 1
      else:
        self.key_values[dir] = 0
    if instr == 'OR':
      if self.key_values[left] == 1 or self.key_values[right] == 1:
        self.key_values[dir] = 1
      else:
        self.key_values[dir] = 0
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.values, self.gates = self.file.split('\n\n')
    self.values = self.values.split('\n')
    self.gates = self.gates.split('\n')[:-1]
    self.key_values = {}
    for line in self.values:
      key, value = line.replace(' ','').split(':')
      self.key_values[key] = int(value)
    
    self.Q = []
    for gate in self.gates:
      left, right, dir = re.findall(r'[a-z|0-9]{3}', gate)
      instr = re.findall(r'[A-Z]+', gate)[0]
      self.Q.append((left, right, dir, instr))
    
  def part1(self):
    while self.Q:
      for i, content in enumerate(self.Q):
        left, right, dir, instr = content
        if left in self.key_values and right in self.key_values:
          self.process_gate(left, right, dir, instr)
          self.Q.pop(i)
          break
    
    z_keys = {k:v for k,v in self.key_values.items() if k.startswith('z')}
    res = ''
    for key in list(reversed(sorted(z_keys))):
      res += str(z_keys[key])
    return int(res, 2)
  
  def part2(self):
    pass
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
