import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file):
    with open(file) as f:
        json_list = []
        for i, values in enumerate(f):
            line = values.strip('\n').split(',')
            if i == 0:
                headers = line
                continue
            json_list.append({})

            for j, _ in enumerate(headers):
                json_list[-1][headers[j]] = line[j]
    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
