import sys 
import time
indent = 20
indentincreasing = False
times = int(input())
try:
    while True:
        print(' ' * indent, end='')
        print('*' * times)
        time.sleep(0.1)

        if indentincreasing:
            indent = indent + 1
            if indent > times:
                break #indentincreasing = False

        else:
            indent = indent - 1
            if indent == 0:
                indentincreasing = True

except KeyboardInterrupt:
    sys.exit()