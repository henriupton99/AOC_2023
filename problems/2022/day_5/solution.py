import argparse

'''
                    [Q]     [P] [P]
                [G] [V] [S] [Z] [F]
            [W] [V] [F] [Z] [W] [Q]
        [V] [T] [N] [J] [W] [B] [W]
    [Z] [L] [V] [B] [C] [R] [N] [M]
[C] [W] [R] [H] [H] [P] [T] [M] [B]
[Q] [Q] [M] [Z] [Z] [N] [G] [G] [J]
[B] [R] [B] [C] [D] [H] [D] [C] [N]
 1   2   3   4   5   6   7   8   9 
'''

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    n_stacks = 3 if test else 9
    self.stacks = [list() for _ in range(n_stacks)]
    self.instructions = []
    for line in self.lines:
      if line.__contains__('['):
        for k in range(n_stacks):
          item = line[k*4:k*4+3]
          if not item.__contains__('['):
            continue
          letter = item.replace('[','').replace(']','').replace(' ','')
          self.stacks[k].append(letter)
      elif line.__contains__('move'):
        instruction = list(map(int,line.replace('move ','').replace('from ','').replace('to ','').split(' ')))
        self.instructions.append(instruction)
    
  def part1(self):
    for instruction in self.instructions:
      number, from_index, to_index = instruction
      for _ in range(number):
        item = self.stacks[from_index-1][0]
        self.stacks[from_index-1].pop(0)
        self.stacks[to_index-1].insert(0,item)
    message = ''.join([stack[0] for stack in self.stacks])
    return message

  def part2(self):
    for instruction in self.instructions:
      number, from_index, to_index = instruction
      slice = self.stacks[from_index-1][:number]
      self.stacks[from_index-1] = self.stacks[from_index-1][number:]
      self.stacks[to_index-1] = slice + self.stacks[to_index-1]
    message = ''.join([stack[0] for stack in self.stacks])
    return message
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
