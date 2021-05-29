
from typing import Sequence


def com():
    #new_list = [expression for memever in interable (if condition)]
    evens = [i for i in range(1,20) if i % 2 == 0]
    print(evens)

    #new_list = [expression (if else condition ) for member in interable]
    a = [1,2,3,4,5,6,7,8,9]
    b = [0 if i < 6 else i for i in a]
    print(b)

    squared = {i : i*i for i in range(1,5)}
    print(squared)

com()