import sys
from collections import defaultdict

import _1_read_log
def get_top_uris(log, n=10):
    hm=defaultdict(int)
    for log_entry in log:
        uri=log_entry[8]
        hm[uri]+=1
    top_ips=sorted(hm, key=hm.get, reverse=True)
    result=[]
    for ip in top_ips[:n]:
        result.append((ip, hm[ip]))
    return result
if __name__=="__main__":
    log=_1_read_log.read_log()
    if len(sys.argv)==2:
        n=int(sys.argv[1])
        print(get_top_uris(log, n))
    else:
        print(get_top_uris(log))