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


def count_power(cubes):
  min_counter = {'red': float('-inf'), 'green': float('-inf'), 'blue': float('-inf')}
  for cube in cubes:
    if cube['red'] > min_counter['red'] and cube['red'] > 1:
      min_counter['red'] = cube['red'] 
    if cube['green'] > min_counter['green'] and cube['green'] > 1:
      min_counter['green'] = cube['green']
    if cube['blue'] > min_counter['blue'] and cube['blue'] > 1:
      min_counter['blue'] = cube['blue']
  min_counter = {x:1 if y == float('-inf') else y for x,y in min_counter.items()}
  
  thepower = min_counter['red'] * min_counter['green'] * min_counter['blue']
  return thepower
      

def main():
  games_dict = file_to_games_dict('input.txt')
  power_list = []

  for game_key in games_dict:
      games = games_dict[game_key]
      power_list.append(count_power(games))
      

  print(power_list)
  print(sum(power_list))

main()