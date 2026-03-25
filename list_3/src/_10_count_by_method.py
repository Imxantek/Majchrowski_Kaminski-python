from _1_read_log import read_log

def count_by_method(log):
    METHOD_INDEX = 6

    method_count_dict = {}

    for logLine in log:
        method = logLine[METHOD_INDEX]
        method_count_dict[method] = method_count_dict.get(method, 0) + 1
    
    return method_count_dict

if __name__ == '__main__':
    log = read_log()
    result_dict = count_by_method(log)
    for key in result_dict:
        print(key, result_dict[key])