def find_all_numbers(input: str) -> str:
    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
        'ten' : '10',
    }
    output = ''
    counter = 0
    for i, char in enumerate(input):
        if char.isdigit():
            output += char 
        for j in range(i+1, len(input)):
            digit_val = digit_map.get(input[i:j+1])
            if digit_val is not None:
                output +=digit_val
    print(output)
    return output

def generate_full_number_list(inputList: list[str]) -> list[int] :
    outputList = []
    for input in inputList:
        output = find_all_numbers(input)
        if len(output) > 1 :
            outputList.append(int(output[0]+output[len(output)-1]))
        else:
            outputList.append(int(output+ output))
    return outputList
        
def find_sum_part_a():
    inputList = parse_input('input1b.txt')
    outputList = generate_full_number_list(inputList)
    return sum(outputList)

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    print(f'sum : {find_sum_part_a()}')


