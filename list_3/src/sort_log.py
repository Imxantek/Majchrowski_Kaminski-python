def sort_log(log, index):
    try:
        return sorted(log, key = lambda x: x[index])
    except IndexError:
        print("Wrong index number")
    except TypeError:
        print("Wrong index type")
    return log # it will not return none