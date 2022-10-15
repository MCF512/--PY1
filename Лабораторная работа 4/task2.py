def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    letters_dict = {}
    default_count = 0
    no_space_str = "".join(str_.lower().split(" "))
    for letter in no_space_str:
        if letter.isalpha():
            letters_dict[letter] = letters_dict.get(letter, default_count) + 1
    return letters_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
