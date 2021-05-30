import sys
def count(n):
    sum = []
    num = 0
    while num < n:
        sum.append(num)
        num +=1
    return sum


def count_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1

# for m in count(100):
#     print(m)
#
# print(sum(count(100)))

#for a in count_generator(100):
#    print(a)
print(sys.getsizeof(count(10000)))
print(sys.getsizeof(count_generator(10000)))


my_generator = {i for i in range(10000)}
list = [i for i in range(10000)]


print(sys.getsizeof(my_generator))
print(sys.getsizeof(list))

