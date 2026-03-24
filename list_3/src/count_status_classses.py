def count_status_classses(log):
    STATUS_INDEX = 14

    # slownik predefiniowany - bez sensu. I tak moga wpadac nowe elementy
    # if code_class in ["2xx", "3xx", "4xx", "5xx"]: - to by trzeba bylo dodac
    
    classes_count = {
        "2xx": 0,
        "3xx": 0,
        "4xx": 0,
        "5xx": 0
    }

    for logLine in log:
        code = logLine[STATUS_INDEX]
        if code.isdigit():
            code_class = code[0] + "xx"
            classes_count[code_class] = classes_count.get(code_class, 0) + 1
    
    return classes_count
    