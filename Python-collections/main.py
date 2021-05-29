from collections import Counter

def counter(a , b=True):

    a = "aaaaaaaaaaaaaaaaacccccccccccbbbbbbbbbbbbbbbb"
    my_counter = Counter(a)
    print(my_counter)
    print(my_counter.most_common(1)) #return a tuple




if __name__ == "__main__":
    counter()
