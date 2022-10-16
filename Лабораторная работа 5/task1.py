from pprint import pprint


def int_dicts(num):
    int_dict = {}
    int_dict.setdefault('bin', bin(num))
    int_dict.setdefault('dec', num)
    int_dict.setdefault('hex', hex(num))
    int_dict.setdefault('oct', oct(num))
    return int_dict


dicts_list = []
for i in range(0, 16):
    dicts_list.append(int_dicts(i))
pprint(dicts_list)