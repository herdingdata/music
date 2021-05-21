import sys
from time import sleep


def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(' ' + str(i))
        sys.stdout.flush()
        sleep(1)
