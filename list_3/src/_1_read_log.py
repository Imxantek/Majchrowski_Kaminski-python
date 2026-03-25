import datetime
import sys

def read_log():
    result=[]
    for line in sys.stdin:
        line=line.strip()
        if line!="":
            fields=line.split("\t")
            if len(fields)<27:
                continue
            ts: datetime.datetime
            id_orig_p: int
            id_resp_p: int
            code: int
            uid=fields[1]
            id_orig_h=fields[2]
            id_resp_h=fields[4]
            method=fields[7]
            host=fields[8]
            uri=fields[9]
            try:
                ts=datetime.datetime.fromtimestamp(float(fields[0]))
                id_orig_p=int(fields[3])
                id_resp_p=int(fields[5])
                code=int(fields[14])
            except ValueError:
                continue
            result.append((ts, uid, id_orig_h, id_orig_p, id_resp_h, id_resp_p, method, host, uri, code))
    return result

if __name__ == '__main__':
    result=read_log()
    print(result)