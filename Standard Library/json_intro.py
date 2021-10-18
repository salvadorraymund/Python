import json
import requests
import csv

data = {
    "president": {
        "name": "Rodrigo Duterte",
        "species": "Betelgeusian"
    }
}

with open("presidens.json", "w") as j:
    json.dump(data, j)

with open('presidens.json', 'r') as j:
    data = json.load(j)
    print(data)

"""Copying data drom json to csv"""
"""a tuple was written on the csv file with a dict as its component"""
with open('presidens.json', 'r') as a_reader, open('copy_customers.csv', 'w') as a_writer:
    data = json.load(a_reader)
    csv_writer = csv.writer(a_writer)
    csv_writer.writerow(data.items())
