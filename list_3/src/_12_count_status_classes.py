from _1_read_log import read_log

def count_status_classes(log):
    STATUS_INDEX = 9

    # slownik predefiniowany - bez sensu. I tak moga wpadac nowe elementy
    # if code_class in ["2xx", "3xx", "4xx", "5xx"]: - to by trzeba bylo dodac
    
    classes_count = {
        "2xx": 0,
        "3xx": 0,
        "4xx": 0,
        "5xx": 0
    }

    for logLine in log:
        code = str(logLine[STATUS_INDEX])
        if code.isdigit():
            code_class = code[0] + "xx"
            classes_count[code_class] = classes_count.get(code_class, 0) + 1
    
    return classes_count

if __name__ == '__main__':
    log = read_log()
    result_dict = count_status_classses(log)
    for key in result_dict:
        print(key, result_dict[key])
    