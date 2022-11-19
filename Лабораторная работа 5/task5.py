import string
from random import sample


def get_random_password(pass_len=8) -> str:
    chars_list = string.digits + string.ascii_lowercase + string.ascii_uppercase
    pass_ = sample(chars_list, pass_len)
    pass_ = "".join(pass_)
    return pass_


print(get_random_password())
