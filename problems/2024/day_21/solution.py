import re
import argparse
from collections import deque
from functools import cache
from itertools import product

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  @staticmethod
  def compute_seqs(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r, c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            possibilities = []
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [(r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">")]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]): continue
                    if keypad[nr][nc] is None: continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1: break
                        optimal = len(moves) + 1
                        possibilities.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = possibilities
    return seqs

  @staticmethod
  def solve(string, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + string, string)]
    return ["".join(x) for x in product(*options)]

  @cache
  def compute_length(self, seq, depth):
    if depth == 1:
        return sum(self.dir_lengths[(x, y)] for x, y in zip("A" + seq, seq))
    length = 0
    for x, y in zip("A" + seq, seq):
        length += min(self.compute_length(subseq, depth - 1) for subseq in self.dir_seqs[(x, y)])
    return length
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.lines = self.file.splitlines()
    self.num_keypad = [
      ["7", "8", "9"],
      ["4", "5", "6"],
      ["1", "2", "3"],
      [None, "0", "A"]
    ]
    self.num_seqs = self.compute_seqs(self.num_keypad)

    self.dir_keypad = [
        [None, "^", "A"],
        ["<", "v", ">"]
    ]
    self.dir_seqs = self.compute_seqs(self.dir_keypad)
    
    self.dir_lengths = {key: len(value[0]) for key, value in self.dir_seqs.items()}
    
  def part1(self):
    total = 0
    depth = 2
    for line in self.lines:
        inputs = self.solve(line, self.num_seqs)
        length = min(map(self.compute_length, inputs, [depth for _ in range(len(inputs))]))
        total += length * int(line[:-1])
    return total
  
  def part2(self):
    total = 0
    depth = 25
    for line in self.lines:
        inputs = self.solve(line, self.num_seqs)
        length = min(map(self.compute_length, inputs, [depth for _ in range(len(inputs))]))
        total += length * int(line[:-1])
    return total
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
