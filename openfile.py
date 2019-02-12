import sys
try:
    with open('aaa.txt','a+') as f:  ### "with" make sure clean up, release
        f.write('HEY!I\'M HERE')
        # str = f.read()
        # print(str)
except OSError as err:
    print("OS Error: {0}",format(err))
except ValueError:
    print("Value Errori")
except:
    print("Unexpected error:", sys.exc_info()[0])


