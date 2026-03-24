import sys
import read_log
def get_entries_by_code(log, code):
    result=[]
    for log_entry in log:
        if log_entry[9]==code:
            result.append(log_entry)
    return result

if __name__ == '__main__':
    if len(sys.argv)<2:
        sys.exit("Usage: python get_entries_by_code.py code < log_file")
    code=int(sys.argv[1])
    log=read_log.read_log()
    print(get_entries_by_code(log, code))
