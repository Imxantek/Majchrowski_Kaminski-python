import os
import sys

def get_env_data(lst: list = None):

    env = dict(os.environ) # tu sa zmienne srodowiskowe z systemu
    res = []

    if lst is None:
        res = sorted(env.items())

    else:
        for key in sorted(lst):
            key=key.upper()
            if key in env:
                res.append((key, env[key]))
            else:
                res.append((key, None))

    return res

if __name__ == "__main__":
    if len(sys.argv)==1:
        data = get_env_data()
    else:
        data = get_env_data(sys.argv[1:])

    for key, value in data:
        if value is None:
            print(f"\"{key}\" is not in env!")
        else:
            print(f"\"{key}\" = {value}")