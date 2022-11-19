import random


def get_unique_list_numbers() -> list[int]:
    list_numbers = []
    while len(list_numbers) != 15:
        num = random.randint(-10, 10)
        if num not in list_numbers:
            list_numbers.append(num)
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))