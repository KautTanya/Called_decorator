"""Called_decorator"""


def called_decorator(func):
    """decorator"""
    def add_text(*args, **kwargs):
        """decorator"""
        print("Function is been called")
        result = func(*args, **kwargs)
        # print(result)
        print("Function is been called")
        return result
    return add_text


@called_decorator
def add_numbers(a, b):
    """example"""
    return a + b


print(add_numbers(8, 7))


# @called_decorator
# def my_function(n):
#     """example"""
#     for i in range(n):
#         print(i)
#
#
# print(my_function(4))
