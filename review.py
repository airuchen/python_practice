tp1 = ()
print(tp1)
tp2 = (1,2,3,4,5,6,7,8)
print(tp2)
print(sum(tp2))
print('=====================')

print(tp2[2:5]) #devide operator
print(tp2[-5:-2]) # countdown

tp3 = tuple([2*x for x in range(1,8)])
print(tp3)

print(range(1,8))
print('=======================')

tp5 = ('John', 'Iven', 'David')
print(tp5)
print(len(tp5))
print(max(tp5))
print(min(tp5))

tp6 = tuple([4,5,2,11,662,43,16,6,83,9,10])
print(tp6)
list1 = list(tp6)
print(list1.sort()) # Just a operation
print(list1)
# print(tp6.sort()) # tuple needs to change into list

print(tp6 == tp5)
tp5 = tp6
print(tp6 == tp5)


