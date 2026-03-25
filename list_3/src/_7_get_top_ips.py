import sys
from collections import defaultdict

import _1_read_log
def get_top_ips(log, n=10):
    hm=defaultdict(int)
    for log_entry in log:
        ip1=log_entry[2]
        ip2=log_entry[4]
        hm[ip1]+=1
        hm[ip2]+=1
    top_ips=sorted(hm, key=hm.get, reverse=True)
    result=[]
    for ip in top_ips[:n]:
        result.append((ip, hm[ip]))
    return result

if __name__=="__main__":
    log=_1_read_log.read_log()
    if len(sys.argv)==2:
        n=int(sys.argv[1])
        print(get_top_ips(log, n))
    else:
        print(get_top_ips(log))