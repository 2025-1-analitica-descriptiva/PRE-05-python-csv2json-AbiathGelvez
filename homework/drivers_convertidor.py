import csv
import json
import os

def convert_csv_to_json(csv_path, json_path):
    drivers = []

    with open(csv_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            drivers.append(row)

    with open(json_path, mode="w", encoding="utf-8") as jsonfile:
        json.dump(drivers, jsonfile, indent=2)

if __name__ == "__main__":
    os.makedirs("files", exist_ok=True)
    convert_csv_to_json("files/drivers.csv", "files/drivers.json")
