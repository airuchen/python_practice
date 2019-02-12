class A(object):
    def __init__(self, a='a'):
        self.a = a
    def print_a(self):
        print(self.a)

class B(object):
    def __init__(self, b='b'):
        self.b = b
    def print_b(self):
        print(self.b)

class C(object):
    def __init__(self, c='c'):
        self.c = c
    def print_c(self):
        print(self.c)

class D(A, B, C):   # polymophism finally come out
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        C.__init__(self)

d = D()
d.print_a()
d.print_b()
d.print_c()
