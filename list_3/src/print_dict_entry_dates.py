import sys
from collections import defaultdict
from log_to_dict import log_to_dict
from read_log import read_log
from entry_to_dict import entry_to_dict
def print_dict_entry_dates(log_dict):
    for uid in log_dict:
        ip_set: set = set()
        host_set: set = set()
        method_dict = defaultdict(int)
        count_2xx: int = 0
        num_requests: int = len(log_dict[uid])
        timestamps=[]
        for entry in log_dict[uid]:
            ip_set.add(entry.get("id_orig_h"))
            ip_set.add(entry.get("id_resp_h"))
            host_set.add(entry.get("host"))
            method_dict[entry.get("method")]+=1
            timestamps.append(entry.get("ts"))
            if int(entry.get("code"))//100==2:
                count_2xx+=1
        first_ts = min(timestamps)
        last_ts = max(timestamps)
        print(f"==== uid: {uid} ====")
        print("first timestamp:")
        print(first_ts)
        print("last timestamp:")
        print(last_ts)
        print("list of all ip addresses:")
        print(ip_set)
        print("list of all hosts:")
        print(host_set)
        print("number of requests:")
        print(num_requests)
        print("Methods proportions:")
        for m_key in method_dict:
            print(f"{m_key}: {100*method_dict[m_key]/num_requests}%")
        print("Code proportions:")
        print(count_2xx,"/",num_requests)
if __name__ == "__main__":
    log=read_log()
    log_dict=log_to_dict(log)
    print_dict_entry_dates(log_dict)
