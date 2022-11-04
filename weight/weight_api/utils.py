from flask import render_template
import db_utils as dbutils
import json
import csv


def upload_in_data(file):
    with open(f"in/{file}") as f:
        if file.endswith(".json"):
            data = json.load(f)
        elif file.endswith(".csv"):
            data = process_csv_file(f)

    for container in data:
        dbutils.batch_weight(container["id"], container["weight"], container["unit"])


def process_csv_file(file):
    data = []
    header = []
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        record = {}
        record[header[0]] = row[0]
        record["weight"] = int(row[1])
        record["unit"] = header[1]
        data.append(record)
    return data


def none_replace(value):
    if value == None:
        value = "na"
    return value


def get_session_json(data):
    session_json = []
    for row in data:
        json_data = {
            "id": none_replace(row[9]),
            "direction": none_replace(row[2]),
            "truck": none_replace(row[3]),
            "bruto": none_replace(row[5]),
        }
        if row[2] == "out":
            json_data["truckTara"] = none_replace(row[6])
            json_data["neto"] = none_replace(row[7])

        session_json.append(json_data)
    return session_json
