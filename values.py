import sys


# Part 1
def read_calibrations(filename):
    """Reads a file and returns a list of integers.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of integers.
    """
    joined_number_list = []
    with open(filename, mode="rt", encoding="utf-8") as f:
        lines = f.readlines()
        for l in lines:
            filtered_list = list(filter(lambda x: x.isdigit(), l))
            if len(filtered_list) < 1:
                joined_number = "".join([filtered_list[0], filtered_list[0]])
            else:
                joined_number = "".join([filtered_list[0], filtered_list[-1]])

            joined_number_list.append(joined_number)
            joined_number_list = [int(i) for i in joined_number_list]
            total = sum(joined_number_list)
    return total


# numbers = [["8", "1", "2", "8", "7"], ["3", "5", "4", "8", "4", "4", "9"], ["1"]]


# def join_numbers(numbers):
#     new_numbers = []
#     for n in numbers:
#         if len(n) < 1:
#             new_number = "".join([n[0], n[0]])
#         else:
#             new_number = "".join([n[0], n[-1]])

#         new_numbers.append(new_number)
#         new_numbers = [int(i) for i in new_numbers]
#         total = sum(new_numbers)
#     return total

# for n in numbers:
#     if len(n) < 1:
#         new_number = "".join([n[0], n[0]])
#     else:
#         new_number = "".join([n[0], n[-1]])

#     new_int = list(new_number)

#     print(new_int)


# def get_numbers(strings):
#     for s in strings:
#         numbers = filter(lambda x: x.isdigit(), s)
#         print(list(numbers))


# Part 2
substring_numbers = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)

strings = (
    "mxmkjvgsdzfhseightonetwo7eight",
    "five34s84four9rtbzllggz",
    "nineninedtfivefive",
    "sixnine6njhqrsix",
)


def find_substring_values(filename):
    """Reads a file, finds substrings for numbers, and converts them to integers.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of integers.
    """

    for s in strings:
        start_string = ""
        end_string = ""
        for sub in substring_numbers:
            if sub in s and s.startswith(sub) and s.endswith(sub):
                start_string_position = s.find(sub) + len(sub)
                start_string = s[:start_string_position]
                end_string_position = len(s) - len(sub)
                end_string = s[end_string_position:]
                joined_strings = [start_string, end_string]
                print("****************")
                print("First: ", start_string)
                print("Last: ", end_string)
                print("****************")
                break
            if sub in s and s.endswith(sub):
                end_string_position = len(s) - len(sub)
                end_string = s[end_string_position:]
                joined_strings = [start_string, end_string]
                print("****************")
                print("Last: ", end_string)
                print("****************")
            if sub in s and s.startswith(sub):
                start_string_position = s.find(sub) + len(sub)
                start_string = s[:start_string_position]
                joined_strings = [start_string, end_string]
                print("****************")
                print("First: ", start_string)
                print("****************")
                break
        print(joined_strings)
