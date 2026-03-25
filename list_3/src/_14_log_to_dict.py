from _1_read_log import read_log
from _13_entry_to_dict import entry_to_dict
from collections import defaultdict

def log_to_dict(log, column_name: str):

    sessions=defaultdict(list)

    for log_entry in log:
        entry_dict=entry_to_dict(log_entry)
        column = entry_dict[column_name]
        sessions[column].append(entry_dict)

    return dict(sessions)

if __name__=="__main__":
    log=read_log()
    print(log_to_dict(log, 'uid'))

# zmodyfikowałem tutaj funkcje - teraz mozna dostac slownik pogrupowny po dowolnej kolumnie w logu
# potrzebne do zadania 18
