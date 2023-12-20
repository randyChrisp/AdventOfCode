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


# strings = ["mxmkjvgsdzfhseightonetwoeight7", "3five4s84four9rtbzllggz"]
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
