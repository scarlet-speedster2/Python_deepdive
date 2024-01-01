# Silly sequence
# Just for fun a custom silly sequence

from functools import lru_cache


class Silly:

    def __init__(self, n):
        self.size = n

    def __getitem__(self, item):
        if item < 0 or item > self.size:
            raise IndexError
        print("get item method is called")
        return "This is the silly item"

    def __len__(self):
        print('len method called')
        return self.size


# s = Silly(10)
#
# for ele in s:
#     print(ele)
#
#
class Fib:

    def __init__(self, size):
        """

        :param size: Size of the Sequence
        """
        self.size = size

    def __getitem__(self, item):
        """

        :param item: it could a int or slice object
        :return: seq or value depending on the item type
        """
        if isinstance(item, int):
            if item < 0:
                item = self.size - item

            if item < 0 or item > self.size:
                raise IndexError

            return Fib._fib(item)
        else:
            range_slice = item.indices(self.size)  # indices require the size to reform the slice
            return [Fib._fib(i) for i in range(*range_slice)]

    @staticmethod
    @lru_cache(maxsize=None)
    def _fib(n):
        """

        :param n: n number of fib element
        :return: nth fib number
        """
        if n < 2:
            return 1

        return Fib._fib(n - 1) + Fib._fib(n - 2)


seq = Fib(20)

print(seq[0])
print(seq[0:15:1])
