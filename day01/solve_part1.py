def file_to_list(filename:str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.rstrip() for x in content]
    return content

def get_calibrated_values(input_string: str) -> int:
    first_number = float("-inf")
    second_number = float("-inf")

    for letter in input_string:
        if letter.isdigit():
            first_number = letter
            break

    for letter in input_string[::-1]:
        if letter.isdigit():
            second_number = letter
            break

    return int(f"{first_number}{second_number}")


def main():
    lines = file_to_list('input.txt')
    calibrated_values = [get_calibrated_values(line) for line in lines]
    total_calibrated = 0
    for value in calibrated_values:
        total_calibrated += value
    print(total_calibrated)
main()

