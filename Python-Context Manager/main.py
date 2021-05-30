from contextlib import contextmanager
from typing import ContextManager
# class ManagerFiles(object):
#   def __init__(self, filename, mode):
#     self.filename = filename
#     self.mode = mode

#   def __enter__(self):
#     print("Open file :" + self.filename)
#     self.open_file = open(self.filename, self.mode)
#     return self.open_file


#   def __exit__(self, type, value, traceback):
#     print("Close file :" + self.filename)
#     self.open_file.close()

# with ManagerFiles("file.txt", "w") as f:
#   print("do some staff..")
#   f.write("Hello, world.")

@contextmanager
def open_file(name , mode):
    f = open(name , mode)
    yield f
    f.close()


with open_file('text.txt' , 'w') as file:
    file.write('testing...')