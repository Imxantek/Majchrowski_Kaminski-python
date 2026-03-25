import sys
from collections import defaultdict
from _1_read_log import read_log

def get_extension_stats(log):
    result=defaultdict(int)
    for log_entry in log:
        uri=log_entry[8]
        if not uri:
            continue

        uri_clean=uri.split("?")[0]
        if not "." in uri_clean or uri_clean.endswith("/"):
            continue
        extension = uri_clean.split(".")[-1]
        if "/" in extension or "\\" in extension:
            continue
        result[extension.lower()] += 1
    return dict(result)
    
if __name__=="__main__":
    log=read_log()
    print(get_extension_stats(log))