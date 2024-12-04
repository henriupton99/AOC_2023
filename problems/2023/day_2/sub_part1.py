import re
configuration = {"red" : 12, "green" : 13, "blue" : 14}

invalid_games_ids = []
sum_games_ids = 0
with open("input.txt") as games:
    for i, game in enumerate(games.readlines()):
        game_id = i+1
        sum_games_ids += game_id
        game = game.replace(f"Game {game_id}:","")
        game_sets = game.split(";")
        for set in game_sets:
            set_colors = set.split(",")
            for color in set_colors:
                color_num = re.search("[0-9]+",color)[0]
                color_name = re.search("[a-z]+",color)[0]
                if int(color_num) > configuration[color_name]\
                    and game_id not in invalid_games_ids:
                    invalid_games_ids.append(game_id)
                    

print(sum_games_ids - sum(invalid_games_ids))