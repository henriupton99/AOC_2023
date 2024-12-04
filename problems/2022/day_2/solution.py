import argparse

class Solution:
  filename_real_input = 'real_input.txt'
  filename_test_input = 'test_input.txt'
  
  def __init__(self, test=False):
    self.file = open(self.filename_test_input,'r').read() if test else open(self.filename_real_input,'r').read()
    self.lines = self.file.splitlines()
    self.item_points = {'X':1,'Y':2,'Z':3}
    
    #A for Rock, B for Paper, and C for Scissors
    #X for Rock, Y for Paper, and Z for Scissors
    self.outcomes_points = {
      'X':{'A':3,'B':0,'C':6},
      'Y':{'A':6,'B':3,'C':0},
      'Z':{'A':0,'B':6,'C':3}
    }
    
  def part1(self):
    self.games_points = []
    for line in self.lines:
      game_points = 0
      plays = line.split(' ')
      opponent_play, my_play = plays
      game_points += self.item_points[my_play]
      game_points += self.outcomes_points[my_play][opponent_play]
      self.games_points.append(game_points)
    return sum(self.games_points)
  
  def part2(self):
    #A for Rock, B for Paper, and C for Scissors
    #X for Rock, Y for Paper, and Z for Scissors
    # X means you need to lose
    # Y means you need to end the round in a draw
    # Z means you need to win
    my_plays = {
      'X':{'A':'Z','B':'X','C':'Y'},
      'Y':{'A':'X','B':'Y','C':'Z'},
      'Z':{'A':'Y','B':'Z','C':'X'}
    }
    self.games_points = []
    for line in self.lines:
      game_points = 0
      plays = line.split(' ')
      opponent_play, strategy = plays
      my_play = my_plays[strategy][opponent_play]
      game_points += self.item_points[my_play]
      game_points += self.outcomes_points[my_play][opponent_play]
      self.games_points.append(game_points)
    return sum(self.games_points)
  
if __name__ == '__main__':
  parser = argparse.ArgumentParser('Solution file')
  parser.add_argument('-part', required=True, type=int, help='Part (1/2)')
  parser.add_argument('-test', required=True, type=str, help='Test mode (True/False)')
  args = parser.parse_args()
  test = True if args.test in ['True','true'] else False
  solution = Solution(test=test)
  result = solution.part1() if args.part == 1 else solution.part2()
  print(f'Result for Part=={args.part} & Test=={test} : {result}')
