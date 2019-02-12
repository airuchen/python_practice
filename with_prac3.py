class File(object):
    def __init__(self, filename, mode):
        # set filename and open mode
        self.filename = filename
        self.mode = mode

    # open file
    def __enter__(self):
        print("open file: ", self.filename)
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    # close file
    def __exit__(self, type, value, trace):
        print("close file: ", self.filename)
        self.open_file.close()

with File("aaa.txt","a") as f:
    print("write")
    f.write("hello, test.")

with File("aaa.txt","r") as f:
    print("Read")
    str = f.read()
    print(str)
