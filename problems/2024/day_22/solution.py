import argparse
import re

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  @staticmethod
  def get_nums(string: str) -> list[int]:
    return list(map(int, re.findall('[-+]?\d+', string)))
  
  @staticmethod
  def mix(value: int, secret_num: int) -> int:
    return value ^ secret_num
  
  @staticmethod
  def prune(value: int) -> int:
    return value % 16777216
  
  @staticmethod
  def get_deltas(prices):
    return [prices[i+1]-prices[i] for i in range(len(prices)-1)]
  
  @staticmethod
  def get_scores(prices, deltas):
    ans = {}
    for i in range(len(deltas)-3):
      pattern = (deltas[i], deltas[i+1], deltas[i+2], deltas[i+3])
      if pattern not in ans:
        ans[pattern] = prices[i+4]
    return ans

  def get_prices(self, secret_num: int, niter: int = 2000) -> int:
    prices = [secret_num]
    for _ in range(niter):
      secret_num = self.prune(self.mix(secret_num * 64, secret_num))
      secret_num = self.prune(self.mix(secret_num // 32, secret_num))
      secret_num = self.prune(self.mix(secret_num * 2048, secret_num))
      prices.append(secret_num)
    return prices
  
  def __init__(self, test=False):
    self.filename = self.filename_test_input if test else self.filename_real_input
    self.file = open(self.filename,'r').read()
    self.secret_nums = list(map(int, self.file.splitlines()))
    
  def part1(self):
    res = 0
    for secret_num in self.secret_nums:
      prices = self.get_prices(secret_num)
      res += prices[-1]
    return res
      
  def part2(self):
    total = {}
    for secret_num in self.secret_nums:
      prices = self.get_prices(secret_num, niter=2000)
      prices = [int(str(p)[-1]) for p in prices]
      deltas = self.get_deltas(prices)
      scores = self.get_scores(prices, deltas)
      
      for k,v in scores.items():
        if k not in total:
          total[k] = v
        else:
          total[k] += v
    return max(total.values())
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
