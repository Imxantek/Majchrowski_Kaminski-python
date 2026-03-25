from _1_read_log import read_log

def get_entries_by_extension(log, ext):

    EXTENSION_INDEX = 8

    filtered_logs_by_extension = []
    for logLine in log:

        uri = logLine[EXTENSION_INDEX]
        uri_cleared = uri.split('?')[0]

        if uri_cleared.endswith("." + ext):
            filtered_logs_by_extension.append(logLine)
    return filtered_logs_by_extension

    # alternative
    # return [logLine for logLine in log if logLine[EXTENSION_INDEX].split('?')[0].endswith("." + ext)]

if __name__ == '__main__':
    log = read_log()
    result = get_entries_by_extension(log, 'jpg')
    for line in result:
        print(line)