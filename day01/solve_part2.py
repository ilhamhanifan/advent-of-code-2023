def file_to_list(filename:str) -> list:
    with open(filename) as f:
        content = f.readlines()
    content = [x.rstrip() for x in content]
    return content

def convert_words_to_numbers(input_string: str) -> int:
    number_words = 'one two three four five six seven eight nine zero'.split(' ')
    number_words_shortend = 'o1e t2o t3e f4r f5e s6x s7n e8t n9e z0o'.split(' ')

    for word in number_words:
        if word in number_words:
            word_index = number_words.index(word)
            input_string = input_string.replace(word, number_words_shortend[word_index])
    return input_string


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
    valid_lines = [convert_words_to_numbers(line) for line in lines]
    calibrated_values = [get_calibrated_values(line) for line in valid_lines]
    total_calibrated = 0
    for value in calibrated_values:
        total_calibrated += value
    print(total_calibrated)
main()



# with open("sample.txt") as f:
#     total_value = 0

#     for line in f:
#         line = convert_letters_to_numbers(line)
#         first_number = float("-inf")
#         second_number = float("-inf")

#         for letter in line:
#             if is_number(letter):
#                 first_number = letter
#                 break

#         for letter in line[::-1]:
#             if is_number(letter):
#                 second_number = letter
#                 break
#         two_digit_number = f"{first_number}{second_number}"
#         total_value += int(two_digit_number)
#         print(two_digit_number)
#     print(total_value)

