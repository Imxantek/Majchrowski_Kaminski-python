import sys
from read_log import read_log
def entry_to_dict(entry):
    return{
        "ts": entry[0],
        "uid": entry[1],
        "id_orig_h": entry[2],
        "id_orig_p": entry[3],
        "id_resp_h": entry[4],
        "id_resp_p": entry[5],
        "method": entry[6],
        "host": entry[7],
        "uri": entry[8],
        "code": entry[9],
    }
if __name__=="__main__":
    log_tuples=read_log()
    log_dicts = [entry_to_dict(e) for e in log_tuples]
    print(log_dicts)
