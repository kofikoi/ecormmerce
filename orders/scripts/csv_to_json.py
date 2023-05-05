import csv
import json
import os

data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

with open(os.path.join(data_dir, 'originalData.csv')) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open(os.path.join(data_dir, 'vehicleData.json'), 'w') as f:
    json.dump(rows, f)