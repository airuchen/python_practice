poem = """fdsafdsafda
fdsafdsafdsafas
fdsafffdggfagds
wgijeijijfdiannllgllg"""

print(len(poem))

fout = open('aaa.txt','wt')
fout.write(poem)
fout.close()

fp = open('aaa.txt','r')
if fp != None:
    str = fp.read()
    print(str)
fp.close()

binaryDate = bytearray(range(0,128))# python3.0 -> bytes(range(0,128))
print(len(binaryDate))

fout = open('binary.bin','wb')
fout.write(binaryDate)
fout.close()

filein = open('binary.bin','rb')
bdata = filein.read()
print(len(bdata))
# for i in len(bdata):
#     print(bdata[i])
filein.close()
