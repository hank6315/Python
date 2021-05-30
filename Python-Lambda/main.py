#lambda arguments : expression

add10 = lambda x: x + 10

'''
def add10_fun(x):
    return x + 10
'''
#print(add10(5))


# mult = lambda x,y: x*y

# print(mult(1,2))


point2D = [[1 , 2], [5 , 1], [-10, 5], [6, 7]]



#point2D_sorted = sorted(point2D , key=lambda x:x[1])
def sort_by_y(x):
    return x[1]

point2D_sorted = sorted(point2D , key=sort_by_y)

print(point2D_sorted)