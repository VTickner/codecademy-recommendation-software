import json
from data import data_dict

def transform_dict(dictionary):
    data_in_categories = {}
    for item, categories in dictionary.items():
        categories_list = categories.split(", ")
        for category in categories_list:
            if category not in data_in_categories:
                data_in_categories[category] = []
            data_in_categories[category].append(item)
    return data_in_categories

def save_transformed_dict(file_path, transformed_dict):
    with open(file_path, "w") as json_file:
        json.dump(transformed_dict, json_file, indent=4)

transformed_dict = transform_dict(data_dict)
save_transformed_dict("data.json", transformed_dict)