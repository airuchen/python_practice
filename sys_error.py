import sys
try:

    f = open('review.py')
    s = f.readline()    # read first line
    s = f.read()        # read whole
    # i = int(s.strip()) # convert to int
    # print(i)
    print(s)

except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexcepted error:", sys.exc_info()[0])
