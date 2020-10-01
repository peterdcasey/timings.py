import time
from typing import Tuple


def time_decorator(fn) -> object:
    """
    Wraps code around the function passed in.
    :param fn: function to decorate
    :return: decorated functtime_ion
    """

    def func(x: object) -> Tuple[int, float]:
        """
        :param x: function object
        :return:
        """
        start = time.time()
        x = fn(x)
        end = time.time()
        return x, end - start

    return func
