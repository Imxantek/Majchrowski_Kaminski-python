from _1_read_log import read_log

def get_unique_methods(log):
    METHOD_INDEX = 6

    unique_methods = set()

    for logLine in log:
        http_method = logLine[METHOD_INDEX]
        unique_methods.add(http_method)
    
    # alternative - Set Comprehension
    # unique_methods = {logLine[METHOD_INDEX] for logLine in log}

    return list(unique_methods)

if __name__ == '__main__':
    log = read_log()
    result = get_unique_methods(log)
    for line in result:
        print(line)