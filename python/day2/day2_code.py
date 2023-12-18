import re
# this function will get the whole list and should do everything
def resolve(lines : list[str]):
    test = [12, 13, 14]
    valid_games = []
    for game_no, line in enumerate(lines, 1):
        sub_games =  line.split(';')
        # print(game_no)
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
    # print(parse_input('example2a.txt'))
    print(resolve(parse_input('input2a.txt')))
