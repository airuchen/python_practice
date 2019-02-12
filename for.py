# tuple
tup = ('python', 2.7, 64)
for i in tup:
    print(i)

# dictionary
dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key, dic[key])

# set
s = set(['python', 'python2', 'python3', 'python'])
for item in s:
    print(item)



# define a Fib class
class Fib(object):
    def __init__(self, max):
        self.max =  max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

# using Fib object
for i in Fib(5):
    print(i)
