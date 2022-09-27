import sys
import time
def spinning_cursor():
    space = ''
    for i in range(100):
        if i%3 == 0:
            s = space + '\\\\  \\\\'
            print(space + '` __o ' + '\n' + s ,end = '')
        if i%3 == 1:
            s = space + '||  ||'
            print(space + '` __o ' + '\n' + s ,end = '')
            space += ' '
        if i%3 == 2:
            s = space +'//  //'
            print(space + '` __o ' + '\n' + s ,end = '')

        time.sleep(0.1)
        print('\r\033[F',end = '')
        
spinning_cursor()
print('\r')
