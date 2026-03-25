from _1_read_log import read_log

def sort_log(log, index):
    try:
        return sorted(log, key = lambda x: x[index])
    except IndexError:
        print("Wrong index number")
    except TypeError:
        print("Wrong index type")
    return log

if __name__ == '__main__':
    log = read_log()
    result = sort_log(log, 3)
    for line in result:
        print(line[3])