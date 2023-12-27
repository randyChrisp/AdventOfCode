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


def find_substring_values(filename):
    """Reads a file, finds substrings for numbers.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of strings.
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


strings = (
    "mxmkjvgsdzfhseightonetwo7eight",
    "five34s84four9rtbzllggz",
    "nineninedtfivefive",
    "sixnine6njhqrsix",
)

substring_key_values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_substrings_sum(filename):
    """Reads a file, finds number substrings and digits.
       Finds the first and last index of the substrings.
       Converts to integers and returns the sum.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of integers.
    """

    def minmax(numbers):
        """Finds the first and last index of the substrings.

        Args:
            numbers (list): A list of integers.

        Returns:
            Tuple: A tuple of integers.
        """

        return min(numbers), max(numbers)

    joined_number_list = []

    for s in strings:
        count = 0
        start_string = ""
        end_string = ""
        # joined_number_list.append(key_index_list)
        key_index_list = []
        for key, value in substring_key_values.items():
            key_index = 0
            start_index = 0
            end_index = None
            if key in s and s.startswith(key) and s.endswith(key):
                start_index = s.find(key)
                key_index_list.append(start_index)
                # start_string_position = s.find(key) + len(key)
                # start_string = s[:start_string_position]
                end_string_position = len(s) - len(key)
                end_string = s[end_string_position:]
                key_index_list.append(end_string_position)
                # joined_number_list.append(key_index_list)
                # print("Start, End ", joined_number_list)
                # joined_strings = [start_string, end_string]
                # joined_number_list = [x for x in key_index_list if x > -1]
                break
            # if key in s and s.endswith(key):
            #     end_string_position = len(s) - len(key)
            #     end_string = s[end_string_position:]
            #     joined_strings = [start_string, end_string]
            # if key in s and s.startswith(key):
            #     start_string_position = s.find(key) + len(key)
            #     start_string = s[:start_string_position]
            #     joined_strings = [start_string, end_string]
            count = s.count(key)
            if count > 1:
                start_index = s.find(key)
                key_index_list.append(start_index)
                end_index = s.rfind(key)
                key_index_list.append(end_index)
                # joined_number_list.append(key_index_list)
                # print("Greater than 1 ", joined_number_list)
            elif s.find(key) > -1:
                key_index = s.find(key)
                key_index_list.append(key_index)
                # joined_number_list.append(key_index_list)
                # print("Else ", joined_number_list)
        joined_number_list.append(key_index_list)
    # print("Key Index List - ", key_index_list)

    # print("Joined Strings: ", joined_strings)
    # print("Joined Number List: ", joined_number_list)

    for n in joined_number_list:
        min_max_values = list(minmax(n))
        print("Min Max Values: ", min_max_values)
        print("Min Max Values: ", min_max_values[0], min_max_values[1])
    # print("****************")
    # print("****************")
    # multiplied_value = value * count
    # print(value, " - ", count, "x")
    # print(multiplied_value)
    # else:
    #     print(value)
