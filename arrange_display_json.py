import json
filename="eq_data_30_day_m1.json"
with open(filename) as f:
    data=json.load(f)

readable_file="readable_eq_data_30.json"
with open(readable_file,'w') as f:
    json.dump(data, f, indent=4)