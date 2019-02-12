import matplotlib.pyplot as mpt

m1 = [1,2,3,4,5,6,7,8,9,10]
m2 = [1,3,4,5,6,7,8,9,10,11]
s1 = [3,6,13,5,1,6,55,8,111,10]
s2 = [55,1,777,32,86,14,654,123,87,3]

mpt.plot(m1,s1,lw=2,label='Iven')
mpt.plot(m2,s2,lw=2,label='John')
mpt.xlabel('m')
mpt.ylabel('dollars')
mpt.legend()
mpt.title('example')
mpt.show()

mpt.plot([1,2,3,4],[6,3,1,9],'r-o') # plot([X-axis],[Y-axis],'plot mark,color')
# mark: '--','s','^'
mpt.axis([0,6],[0,15])  # axis([x-start,x-end],[y-start,y-end])
mpt.show()

