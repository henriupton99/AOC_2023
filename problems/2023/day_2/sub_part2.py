import re

with open("input.txt") as games:
    games_powers = []
    for i, game in enumerate(games.readlines()):
        min_num_per_color = {"blue" : 0, "red" : 0, "green" : 0}
        game_id = i+1
        game = game.replace(f"Game {game_id}:","")
        game_sets = game.split(";")
        for set in game_sets:
            set_colors = set.split(",")
            for color in set_colors:
                color_num = re.search("[0-9]+",color)[0]
                color_name = re.search("[a-z]+",color)[0]
                if int(color_num) > min_num_per_color[color_name]:
                    min_num_per_color[color_name] = int(color_num)
        
        game_power = 1
        for color_num in min_num_per_color.values():
            game_power *= color_num
        
        games_powers.append(game_power)

print(sum(games_powers))
        