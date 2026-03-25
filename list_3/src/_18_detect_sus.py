from _1_read_log import read_log
from _14_log_to_dict import log_to_dict
import statistics

def detect_sus(log, treshold: int):

    ip_dict = log_to_dict(log, "id_orig_h")
    ip_count = {}
    sus_ip_set = set()

    for ip, ip_list in ip_dict.items():
        ip_count[ip] = len(ip_list)

        if(len(ip_list) > treshold):
            sus_ip_set.add(ip)
    
    median = statistics.median(ip_count.values())
    mean = statistics.mean(ip_count.values())

    return sus_ip_set, median, mean

if __name__=="__main__":
    log = read_log()
    sus_set, median, mean = detect_sus(log, 500)
    print(sus_set)
    print("median of attempts per IP: ",  median)
    print("mean of attepts per IP: ", mean)
