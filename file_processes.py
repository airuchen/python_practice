fp = open('aaa.txt','a')
if fp != None:
    print('success to open file')
fp.close()

fp = open('aaa.txt','r+')
if fp!= None:
    str = fp.read()
    print(str)
fp.close()

fp = open('aaa.txt','a+')
if fp != None:
    fp.write('fdsafdsafdsa')
fp.close()

fp = open('aaa.txt','r+')
if fp != None:
    str = fp.read()
    print(str)
fp.close()

