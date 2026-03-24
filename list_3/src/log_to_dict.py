import sys
from read_log import read_log
from entry_to_dict import entry_to_dict
from collections import defaultdict

def log_to_dict(log):
    sessions=defaultdict(list)
    for log_entry in log:
        entry_dict=entry_to_dict(log_entry)
        uid=entry_dict['uid']
        sessions[uid].append(entry_dict)
    return dict(sessions)
if __name__=="__main__":
    log=read_log()
    print(log_to_dict(log))