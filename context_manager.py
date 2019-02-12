from contextlib import contextmanager

@contextmanager
def open_file(name, mode):
    f = open(name, mode)
    yield f
    f.close()

with open_file('aaa.txt', 'r') as f:
    print(f.read())
