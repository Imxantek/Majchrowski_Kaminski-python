import sys
import read_log
def get_failed_reads(log, merge=False):
    res4=[]
    res5=[]
    for log_entry in log:
        if log_entry[9]/100==4:
            res4.append(log_entry)
        elif log_entry[9]/100==5:
            res5.append(log_entry)
    if merge:
        return res4+res5
    else:
        return res4, res5
if __name__=="__main__":
    log=read_log.read_log()
    if len(sys.argv)<2:
        merge=bool(sys.argv[1])
        print(get_failed_reads(log, merge))
    else:
        print(get_failed_reads(log))