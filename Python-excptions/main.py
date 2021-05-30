class ValuetoHighError(Exception):
    pass


class ValuetoSmallError(Exception):
    def __init__(self , message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValuetoHighError('Value is to high')
    if x < 5 :
        raise ValuetoSmallError('Value is to Small', x)

#test_value(1)


try:
    test_value(1)
except ValuetoHighError as e:
    print(e)
except ValuetoSmallError as e:
    print(e.message , e.value)