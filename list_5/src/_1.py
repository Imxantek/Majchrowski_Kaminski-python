import csv
import datetime
from collections import namedtuple

Measurement = namedtuple("Measurement", ["time", "value"])
Data= namedtuple("Data", ["Nr", "StationCode", "indicator", "AvgingTime", "unit", "PositionCode"])

def parse_stations(path="../data/stacje.csv"):
    result: dict[str, list[str]] = {}
    try:
        with (open(path, 'r', encoding='utf-8') as csvfile):
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row["Nr"] not in result:
                    result[row["Nr"]] = []

                for key in row.keys():
                    if key == "Nr":
                        continue

                    result[row["Nr"]].append(row[key])

    except FileNotFoundError:
        print("File not found")

    return result


def parse_measurements(path="../data/2023_PM10_1g.csv"):
    result: dict[Data, list[Measurement]] = {}
    try:
        with open(path, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            header_rows = []
            for i in range(6):
                header_rows.append(next(reader)[1:])

            # zip - kolumny w krotki
            # gwiazdka rozbija nam liste na poszczegolne kolumny
            columns = list(zip(*header_rows))
            keys_idx = []
            for col in columns:
                tup = Data(*col)
                result[tup] = []
                keys_idx.append(tup)

            for row in reader:
                if not row or not row[0].strip():
                    continue

                date_str = row[0].strip()

                try:
                    full_dt = datetime.datetime.strptime(date_str, "%m/%d/%y %H:%M")
                except ValueError:
                    print(f"BŁĄD: Nie mogę sparsować daty: {row[0]}")
                    break

                for idx, value in enumerate(row[1:]):
                    val = None

                    if value.strip():
                        try:
                            val = float(value.strip().replace(",", "."))
                        except ValueError:
                            val = None

                    current_key = keys_idx[idx]
                    result[current_key].append(Measurement(full_dt, val))

    except FileNotFoundError:
        print("File not found")
    return result

if __name__ == '__main__':
    station_info = parse_stations()
    for station in station_info:
        print(station, " ", station_info[station])
    print(parse_measurements())
