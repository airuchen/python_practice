import sys

def displaySalary(salary):
    if salary<0:
        raise ValueError('positive')
    print('Salary = '+str(salary))
while True:
    try:
        Salary = float(input('enter Salary:'))
        displaySalary(Salary)
        break
    except OSError as err:
        print('OS Error: {0}'.format(err))
    except ValueError:
        print('Error: Enter positive value')
    except:
        print('Unexpected error:', sys.exc_info()[0])
