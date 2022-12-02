
def compute_score(oponent_move, player_move):
  OPONENT_MOVE = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3 # Scissors
  }

  PLAYER_MOVE = {
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3 # Scissors
  }

  SCORE_MAP = {
    "A": {
      "X": 3,
      "Y": 6,
      "Z": 0
    },
    "B": {
      "X": 0,
      "Y": 3,
      "Z": 6
    },
    "C": {
      "X": 6,
      "Y": 0,
      "Z": 3
    }
  }
  
  return SCORE_MAP[oponent_move][player_move] + PLAYER_MOVE[player_move]

def part1():


  f = open("./input.txt", "r")

  score = 0
  for move in f.read().splitlines():
    oponent_move, player_move = move.split(" ")
    score += compute_score(oponent_move, player_move)
  print(score)

def part2():
  f = open("./input.txt", "r")

  MOVE_MAP = {
      "A":{
        "X": "Z",
        "Y": "X",
        "Z": "Y"
      },
      "B":{
        "X": "X",
        "Y": "Y",
        "Z": "Z"
      },
      "C":{
        "X": "Y",
        "Y": "Z",
        "Z": "X"
      }
  }

  score = 0
  for move in f.read().splitlines():
    oponent_move, match_result = move.split(" ")
    score += compute_score(oponent_move, MOVE_MAP[oponent_move][match_result])
  print(score)

part1()
part2()