from pprint import pprint


def int_dicts(num):
    int_dict = {}
    int_dict.setdefault('bin', bin(num))
    int_dict.setdefault('dec', num)
    int_dict.setdefault('hex', hex(num))
    int_dict.setdefault('oct', oct(num))
    return int_dict


dicts_list = [int_dicts(i) for i in range(0, 16)]
pprint(dicts_list)
