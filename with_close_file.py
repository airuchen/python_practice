fp = open('with.txt','w')
fp.write("aaaaaaaa")
fp.close()

with open('with.txt','r') as fileIn:
    data = fileIn.read()
    print(data)
