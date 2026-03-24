from entry_to_dict import entry_to_dict

def log_to_dict(log):
    UID_INDEX = 1
    uid_dict = {}

    for logLine in log:
        uid = logLine[UID_INDEX]
        entry =  entry_to_dict(logLine)
        uid_dict.setdefault(uid, []).append(entry)
    
    return uid_dict