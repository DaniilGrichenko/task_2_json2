import json
import csv
import argparse

results = {
    "ip_str": [],
    "country_code": [],
    "postal_code": [],
    "country_name": []
}

with open('Task_2_1.json', 'r') as file:
    json_data = json.load(file)

def find_key_values(data, target_keys, results):
    if isinstance(data, dict):
        for key, value in data.items():
            if key in target_keys:
                results[key].append(value)
            elif isinstance(value, (dict, list)):
                find_key_values(value, target_keys, results)

    elif isinstance(data, list):
        for item in data:
            find_key_values(item, target_keys, results)

find_key_values(json_data, results.keys(), results)

if results:
    for key, value in results.items():
        pass
else:
    print(f"Не знайденно JSON-фафл")

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-j", "--json", action="store_true")
group.add_argument("-c", "--csv", action="store_true")
group.add_argument("--console", action="store_true")
args = parser.parse_args()

if args.json:
    json_filename = "results.json"
    with open(json_filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    pass

if args.csv:
    csv_filename = "results.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(results.keys())  
        writer.writerows(zip(*results.values()))  
    pass

if args.console:
    for key, value in results.items():
        print(f"Значення ключа '{key}': {value}")