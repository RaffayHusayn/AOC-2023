def find_all_numbers(input: str) -> str:
    output = ''
    for char in input:
        if char.isdigit():
            output += char 
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
    inputList = parse_input('input.txt')
    outputList = generate_full_number_list(inputList)
    return sum(outputList)

def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    print(f'sum : {find_sum_part_a()}')


