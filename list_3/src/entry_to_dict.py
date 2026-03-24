def entry_to_dict(logLine):
    return {
        "ts": logLine[0],
        "uid": logLine[1],
        "ip": logLine[2],
        "port": logLine[3],
        "dest_ip": logLine[4],
        "dest_port": logLine[5],
        "method": logLine[7],
        "host": logLine[8],
        "uri": logLine[9],
        "user_agent": logLine[11],
        "status_code": logLine[14],
        "status_msg": logLine[15]
    }