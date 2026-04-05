import os
import sys
import time
from collections import deque

def tail():

    lines = 10
    file_path=None
    follow=False
    args=sys.argv[1:]
    clean_args=[]

    for arg in args:
        if arg.startswith("--lines="):
            lines=int(arg.split("=")[1])
        elif arg=="--follow":
            follow=True
        else:
            clean_args.append(arg)

    input_source=None

    if clean_args:
        file_path=clean_args[0]
        try:
            input_source=open(file_path,"r")
        except FileNotFoundError:
            print("File not found")
            return
    # sprawdzamy czy argument jest pipem
    elif not sys.stdin.isatty():
        input_source=sys.stdin
    else:
        print("Usage: python tail.py [--lines=<int>] [--follow]")

    buffer=deque(input_source, maxlen=lines)
    for line in buffer:
        print(line, end='')

    if follow and file_path:
        try:
            input_source.seek(0, os.SEEK_END)
            while True:
                line=input_source.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                print(line, end='')
        except KeyboardInterrupt:
            pass

    if input_source is not sys.stdin:
        input_source.close()

if __name__ == '__main__':
    tail()