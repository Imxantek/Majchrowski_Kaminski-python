import argparse
import datetime
import csv
import random
import _6
from statistics import *
from collections import namedtuple

parser = argparse.ArgumentParser(
        prog="python list_5.py, ex5",
        description="lol"
    )

Measurement = namedtuple('Measurement', ['time', 'value'])

def get_data_from_code(code:str):
    global parser
    path="../data/stacje.csv"

    try:
        with (open(path, 'r', encoding='utf-8') as csvfile):
            _6.logger.info(f"reading file {path}")
            reader = csv.DictReader(csvfile)

            if not reader:
                _6.logger.warning(f"provided data file {path} is empty")

            for row in reader:
                byte_data=(",".join(row.values()).encode('utf-8'))
                size=len(byte_data)
                _6.logger.debug(f"Read {size} bytes")

                if row['Kod stacji'] == code:
                    _6.logger.info(f"closing file {path}")
                    return row

    except FileNotFoundError:
        _6.logger.error(f"missing data file for {code}")
        parser.error(f"couldn't find such station {code}")

def parse_csv_data(args):
    global parser
    year = args.start.year
    freq = args.freq
    type = args.type
    parsed_data = {}

    if args.type == "PM2.5":
        type = "PM25"

    path = "../data/" + str(year) + "_" + str(type) + "_" + str(freq) + ".csv"

    try:
        with open(path, "r", encoding="utf-8") as csvfile:
            _6.logger.info(f"reading file {path}")
            reader = csv.reader(csvfile)

            if not reader:
                _6.logger.warning(f"provided data file {path} is empty")

            byte_data:bytes
            size:int

            for i in range(5):
                line=next(reader)
                byte_data=",".join(line).encode('utf-8')
                size=len(byte_data)
                _6.logger.debug(f"Read {size} bytes")

            full_row = next(reader)
            position_row = full_row[1:]
            byte_data=",".join(full_row).encode('utf-8')
            size=len(byte_data)
            _6.logger.debug(f"Read {size} bytes")

            for code in position_row:
                if code.strip():
                    parsed_data[code] = []

            for row in reader:
                byte_data=",".join(row).encode('utf-8')
                size=len(byte_data)
                _6.logger.debug(f"Read {size} bytes")

                if not row:
                    continue

                try:
                    full_dt = datetime.datetime.strptime(row[0].strip(), "%m/%d/%y %H:%M")
                except ValueError:
                    _6.logger.error(f"invalid date format in provided file: {row[0]} - is not mm-dd-YYYY HH:MM")
                    break

                date = full_dt.date()

                if date<args.start:
                    continue

                if date > args.end:
                    break

                else:
                    for idx, code in enumerate(position_row):

                        if not code.strip():
                            continue

                        val = None
                        value_str = ""

                        if (idx + 1) < len(row):
                            value_str = row[idx + 1].strip()

                        if value_str:
                            try:
                                val = float(value_str.replace(",", "."))
                            except ValueError:
                                _6.logger.error(f"invalid value format in provided file: {row[idx]}")
                                val = None

                        parsed_data[code].append(Measurement(date, val))
        _6.logger.info(f"closing file {path}")
    except FileNotFoundError:
        _6.logger.error(f"missing data file for {path}")
        parser.error(f"missing data file for {path}")

    return parsed_data

def random_logic(args):
    active_stations = []

    for code, measurements in parse_csv_data(args).items():
        if len(measurements) > 0:
            active_stations.append(code)

    if not active_stations:
        _6.logger.warning("no active stations in this period of time")
        print("no active stations in this period of time")
        return

    print("selected station:")
    selected_station = random.choice(active_stations).split("-")[0]
    print(selected_station)
    print("Station data: ")
    print(get_data_from_code(selected_station))

def stats_logic(args):
    data=parse_csv_data(args)
    key=args.station+"-"+args.type+"-"+args.freq

    if key not in data:
        _6.logger.error(f"no such station: {args.station} in this period of time")
        print(f"no such station: {args.station} in this period of time")
        return

    print("selected station:")
    print(key)
    measurements:list[float]=list()

    for mmnt in data[key]:
        if mmnt.value is not None:
            measurements.append(mmnt.value)

    if args.station not in data:
        _6.logger.warning(f"no results for station: {args.station} in this period of time")

    if len(measurements)==0:
        print("not enough measurements to calculate the average")

    elif len(measurements)==1:
        print("average: ")
        print(mean(measurements))
        print("not enough measurements to calculate the std deviation")

    else:
        avg=mean(measurements)
        std_dev=stdev(measurements)
        print("average: ")
        print(avg)
        print("standard deviation: ")
        print(std_dev)


def valid_date(date):
    try:
        return datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"{date} is not a valid date")

def main():
    global parser
    parser.add_argument("-t", "--type", required=True, choices=["PM10", "PM2.5", "NO"],
                        help="measured type. avb choices: PM10, PM2.5, NO")

    parser.add_argument("--freq", required=True, choices=["1g", "24g"],
                        help="measured frequency. avb choices: 1g, 24g")

    parser.add_argument("--start", required=True, type=valid_date, help="measured from. format (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, type=valid_date, help="measured until. format (YYYY-MM-DD)")

    subparsers = parser.add_subparsers(dest="command", required=True, help="suboperations. avb choices: random, stats")

    random=subparsers.add_parser("random", help="returns a random station that measures provided values")
    stats=subparsers.add_parser("stats", help="calculates the average and std deviation of scores with provided type")
    stats.add_argument("--station", required=True, help="station name")

    args = parser.parse_args()

    if args.start>args.end:
        parser.error(f"{args.start} is after {args.end}")

    if args.command == "random":
        random_logic(args)
    else:
        stats_logic(args)

if __name__ == "__main__":
    main()