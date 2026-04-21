import csv
import re


def parse_names(string: str) -> str:
    result=string
    polish="ąćęłńóśźżĄĆĘŁŃÓŚŹŻ "
    english="acelnoszzACELNOSZZ_"
    for i in range(len(polish)):
        result=re.sub(polish[i],english[i],result)
    return result

def print_file(path="../data/stacje.csv"):
    op_dates:list[str]=list()
    cl_dates:list[str]=list()
    widths:list[float]=list()
    lengths:list[float]=list()
    dashed_stations:list[str]=list()
    modified_names:list[str]=list()
    mobile_check:bool=True
    three_sections:list[str]=list()
    street_names:list[str]=list()

    with (open(path, 'r', encoding='utf-8') as csvfile):
        reader = csv.DictReader(csvfile)
        for row in reader:
            name=row['Nazwa stacji']
            # point a
            # 4 dig + - + 2 dig + - + 2 dig
            if re.fullmatch(r'\d{4}-\d{2}-\d{2}',row['Data uruchomienia']):
                op_dates.append(row['Data uruchomienia'])

            # 4 dig + - + 2 dig + - + 2 dig
            if re.fullmatch(r'\d{4}-\d{2}-\d{2}', row['Data zamknięcia']):
                cl_dates.append(row['Data zamknięcia'])


            # point b
            # some digits + . + 6 digits
            if re.fullmatch(r'\d+\.\d{6}',row['WGS84 φ N']):
                widths.append(float(row['WGS84 φ N']))
            # some digits + . + 6 digits
            if re.fullmatch(r'\d+\.\d{6}', row['WGS84 λ E']):
                lengths.append(float(row['WGS84 λ E']))


            # point c
            #start (no -) + - + (no -) end
            if re.match(r'^[^-]+-[^-]+$', name):
                dashed_stations.append(name)

            # point d
            modified_names.append(parse_names(name))


            # point e
            #check if ends with mob
            if re.search(r'MOB$',row['Kod stacji']):
                #check if mobilna
                if not re.fullmatch(r'mobilna', row['Typ stacji']):
                    mobile_check=False


            # point f
            # start (no -) + - +(no -) + - + (no -) end
            if re.match(r'^[^-]+-[^-]+-[^-]+$', name):
                three_sections.append(name)


            # point g
            #find comma then any amt of any chr and later ul or al
            if re.search(r',.*(ul\.|al\.)', name):
                street_names.append(name)


    print("===1===")
    print(op_dates)
    print(cl_dates)

    print("\n===2===")
    print(widths)
    print(lengths)

    print("\n===3===")
    print(dashed_stations)

    print("\n===4===")
    print(modified_names)

    print("\n===5===")
    print(mobile_check)

    print("\n===6===")
    print(three_sections)

    print("\n===7===")
    print(street_names)

if __name__ == '__main__':
    print_file()