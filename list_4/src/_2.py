import os
from _1 import get_env_data
import sys

def get_catalogues(path_data, with_files=False):

    path_split = path_data.strip().split(';')

    for path in path_split:
        print(path)
        if with_files:
            try:
                for file in os.listdir(path):
                    print(" "+file)
            except FileNotFoundError:
                print(" Could not find files")

def convert_to_boolean(decision : str):
    return decision == "True"

if __name__ == '__main__':
    lst=["PATH"]
    env = get_env_data(lst)

    #pobierane przez nas dane znajduja sie w drugiej wartosci pierwszej krotki
    path_data = env[0][1]
    if len(sys.argv)==1:
        get_catalogues(path_data)
    elif len(sys.argv)==2 and (sys.argv[1] == "False" or sys.argv[1] == "True"):
        with_files = convert_to_boolean(sys.argv[1])
        get_catalogues(path_data, with_files)
    else:
        print("Wrong number of arguments")
        print("Usage: python _2.py True/False")