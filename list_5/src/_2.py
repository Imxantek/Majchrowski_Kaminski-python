import os
import re
def group_measurements_files_by_key(path="../data"):
    result: dict[tuple[int, str, str], str] ={}
    with os.scandir(path) as entries:
        for entry in entries:
            # 4 cyfry _ znak niebiały raz lub więcej _ jedna lub dwie cyfry, znak niebiały i .csv
            if re.fullmatch(r'\d{4}_\S+_(\d|\d{2})\S\.csv',entry.name):
                print(entry.name)
                split=re.split('_',entry.name)
                year=int(split[0])
                type=split[1]
                freq=str(re.split('\.',split[2])[0])
                tup=(year,type,freq)

                if tup not in result:
                    result[tup]="../data/"+entry.name

    return result
if __name__=="__main__":
    print(group_measurements_files_by_key())