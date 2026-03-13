import json
import csv

def save_to_json(data, filename="report.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_to_csv(data_list, filename="history.csv"):
    keys = data_list[0].keys()
    with open(filename, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)
