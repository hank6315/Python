
from typing import Sequence
#from tqdm import trange
import time 
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

#com()


# temp = 0
# total = 1000

# for n in range(1000):
#     temp += 1
#     print('\r' + '[Progress]:[%s%s] %.2f%% %d/%d;' % (
#     '█' * int(temp*20/total), ' ' * (20-int(temp*20/total)),
#     float(temp/total*100), temp,total), end='')
#     time.sleep(0.001)