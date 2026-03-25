import ipaddress
from _1_read_log import read_log

def get_entries_by_addr(log, addr):
    '''IPv4Address(addr) creates an object out of the addr. If not correct it throws a valueExcept'''
    IPv4_INDEX = 2

    try:
        ipaddress.IPv4Address(addr)
    except ValueError:
        print("This is not a valid IPv4")
        return []
    
    '''List Comprehensions (wyrazenie listowe) - creates a list out of a loop expression'''
    return [logLine for logLine in log if logLine[IPv4_INDEX] == addr]

if __name__ == '__main__':
    log = read_log()
    result = get_entries_by_addr(log, '192.168.202.79')
    for line in result:
        print(line)