def count_by_method(log):
    METHOD_INDEX = 7

    method_count_dict = {}

    for logLine in log:
        method = logLine[METHOD_INDEX]
        method_count_dict[method] = method_count_dict.get(method, 0) + 1
    
    return method_count_dict