import random


def get_random_password() -> str:
    chars_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefjhijklmnopqrstuvwxyz123456789"
    pass_ = random.sample(chars_list, 8)
    pass_ = "".join(pass_)
    return pass_


print(get_random_password())
