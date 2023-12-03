def parse_games(games):
  parsed_games = []
  for game in games:
    cubes = {"red":0, "green":0, "blue":0 }
    game = game.split(", ")
    for cube in game:
      if "red" in cube:
        cubes["red"] += int(cube[:-4])
      elif "green" in cube:
        cubes["green"] += int(cube[:-6])
      elif "blue" in cube:
        cubes["blue"] += int(cube[:-5])
    parsed_games.append(cubes)
  return parsed_games

def file_to_games_dict(filename:str) -> list:
    with open(filename) as f:
      contents = f.readlines()
      games_dict = {}
      for content in contents:
        content = content.strip()

        game_key, games = content.split(": ")
        game_key = int(game_key.lstrip("Game "))
        games = games.split("; ")

        games = parse_games(games)

        games_dict[game_key] = games

    return games_dict


def validate_games(cubes, rule):
  # {'red': 12, 'green': 13, 'blue': 14}
  for cube in cubes:
    if cube['red'] > rule['red']:
      return False
    elif cube['green'] > rule['green']:
      return False
    elif cube['blue'] > rule['blue']:
      return False
    continue
  return True
      

def main():
  games_dict = file_to_games_dict('input.txt')
  rule = {'red': 12, 'green': 13, 'blue': 14}
  valid_games = []

  for game_key in games_dict:
    if validate_games(games_dict[game_key], rule):
      valid_games.append(game_key)
      

  print(valid_games)
  print(sum(valid_games))

main()
