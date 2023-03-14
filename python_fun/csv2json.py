import csv
import json

fieldnames = ("header_1", "header_2", "header_3", "header_4")


def csv2json(file: str):
    try:
        csv_file = open(file, 'r')
    except:
        csv_file = open(file, encoding='UTF-16')
    finally:
        json_file = open('file.json', 'w')
        fieldnames = ("coma", "separated", "columns")
        reader = csv.DictReader(csv_file, fieldnames)
        for row in reader:
            json.dump(row, json_file)
            json_file.write('\n')
