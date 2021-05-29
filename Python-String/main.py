from timeit import default_timer as timer

def timecomare():
    my_list = ['a'] * 1000000
    #print(my_list)

    #bad
    start = timer()
    my_string = ''
    for i in my_list:
        my_string += i
    stop = timer()
    print(stop - start)

    #good
    start = timer()
    my_string = ''.join(my_list)
    end = timer()
    print(end - start)


#format
def format():
    var = 3.12345
    my_string = "the var is {}".format(var)
    print(my_string)

    my_string_2 = "the var is {:.2f}".format(var)
    print(my_string_2)

    my_string_3 = f"the var is {var}"
    print(my_string_3)


if __name__ == '__main__':
    #format()