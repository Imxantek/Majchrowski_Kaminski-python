import datetime
import sys
import _1_read_log
def get_entries_in_time_range(log, start, end):
    dt_start=datetime.datetime.fromtimestamp(start)
    dt_end=datetime.datetime.fromtimestamp(end)
    result=[]
    for log_line in log:
        if dt_start <= log_line[0] <= dt_end:
            result.append(log_line)
    return result
if __name__=="__main__":
    log=_1_read_log.read_log()
    if(len(sys.argv)<3):
        sys.exit("Usage: python get_entries_in_time_range.py start end < log_file ")
    start=float(sys.argv[1])
    end=float(sys.argv[2])
    print(get_entries_in_time_range(log, start, end))