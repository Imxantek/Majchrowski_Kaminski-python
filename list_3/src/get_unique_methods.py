def get_unique_methods(log):
    METHOD_INDEX = 7

    unique_methods = set()

    for logLine in log:
        http_method = logLine[METHOD_INDEX]
        unique_methods.add(http_method)
    
    # alternative - Set Comprehension
    # unique_methods = {logLine[METHOD_INDEX] for logLine in log}

    return list(unique_methods)