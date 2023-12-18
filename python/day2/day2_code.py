import re
from functools import reduce

# Solves for part 2A
def sum_of_valid_games_2a(lines : list[str]):
    test = [12, 13, 14]
    valid_games = []
    for game_no, line in enumerate(lines, 1):
        sub_games =  line.split(';')
        all_sub_games_valid: list[bool] = []
        for sub in sub_games:
            colors = parse_colors(sub)
            if all(x <= y for x,y in zip(colors, test)):
                print(f'valid sub game | game = {game_no} | {colors}')
                all_sub_games_valid.append(True)
            else : 
                print(f'in valid sub game | game = {game_no} | {colors}')
                all_sub_games_valid.append(False)
        if all(all_sub_games_valid):
            valid_games.append(game_no)
    print(valid_games)
    return sum(valid_games)


# Solves for part 2B
def part_2b(lines : list[str]) :
    total_sum = 0
    for game_no, line in enumerate(lines):
        ind_game_prod = 1
        sub_games = line.split(';')
        highest_color = [0,0,0]
        for sub in sub_games:
            colors = parse_colors(sub)
            for index,(x,y) in enumerate(zip(highest_color, colors)):
                if x < y:
                    highest_color[index] = y
        print(f'lowest colors needed for game # {game_no} = {highest_color}')
        total_sum = total_sum+ reduce(lambda x,y : x*y, highest_color)

    return total_sum


def parse_colors(input_string) -> list[int]:
    # Define a regular expression pattern for matching the count and color
    color_pattern = re.compile(r'(\d+)\s*(green|red|blue)\b')
    # Find all matches in the input string
    matches = color_pattern.findall(input_string)
    # Extract counts and colors from the matches
    result = [0, 0, 0]
    for count, color in matches:
        if color == 'red':
            result[0] = int(count)
        elif color == 'green':
            result[1] = int(count)
        elif color == 'blue':
            result[2] = int(count)
    return result




def parse_input(filename : str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    # print(sum_of_valid_games_2a(parse_input('input2a.txt')))
    print(part_2b(parse_input('input2b.txt')))
