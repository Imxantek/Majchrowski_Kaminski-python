import csv
from tokenize import group
from typing import Optional
import re

def get_addresses(city, path="../data/stacje.csv"):
    # województwo, miasto, ulica, opcjonalnie: numer
    result: list[tuple[str, str, str, Optional[int]]]=list()
    with open(path,'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if re.fullmatch(city, row["Miejscowość"]):
                address = row["Adres"].strip()
                street = address
                number = None

                # (((dowolny znak) zero lub wiele razy) zero lub jeden raz)
                # whitespace jeden lub wiecej
                # jedna lub wiecej cyfr
                # dowolna ilość dowolnej litery
                match = re.search(r'^(.*?)\s+(\d+)[a-zA-Z]*$', address)

                if match:
                    # (.*?)
                    street = match.group(1).strip()
                    # (\d+)
                    number = int(match.group(2))


                split=re.split(" ", row["Adres"].strip())
                tup=(row["Województwo"], row["Miejscowość"], street, number)
                result.append(tup)

    return result
if __name__ == "__main__":
    print(get_addresses("Wrocław"))