import sys
from collections import defaultdict
from _14_log_to_dict import log_to_dict
from _1_read_log import read_log

def get_session_paths(log):
    log_dict=log_to_dict(log)
    result=defaultdict(list)
    for uid in log_dict:
        for entry in log_dict[uid]:
            result[uid].append(entry.get("uri"))
    return dict(result)

if __name__=="__main__":
    log=read_log()
    result=get_session_paths(log)
    print(result)