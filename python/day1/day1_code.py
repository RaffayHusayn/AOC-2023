input = "1Absdfjkh"

def find_number(inputList : list[str]) -> list[str]:
    outputList = []
    for input in inputList:
        output = ""
        for char in input:
            if char.isdigit():
                output += char
            if(len(output) == 2):
                break

        if(len(output) < 2):
            output +=output
        outputList.append(output)
    return outputList 
    



def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]



if __name__ == '__main__':
    # print(parse_input('example.txt'))
    print(find_number(parse_input('example.txt')))


