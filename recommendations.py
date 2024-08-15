import json
from data import data_items, data_categories
from classes.stack import Stack

def load_transformed_dict(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

data_items = data_items
data_categories = data_categories
items_in_categories = load_transformed_dict("data.json")
categories = [category for category in items_in_categories.keys()]
sorted_categories = sorted(set(categories))
selected_categories = Stack()

def welcome():
    number_items = len(set([item for items in items_in_categories.values() for item in items]))
    print(f"\nWelcome to {data_items} recommendation software where there are {number_items} {data_items} to choose from!")
    print(f"Recommendations are chosen from the {data_categories} that you select. So let's get started...\n")

def get_category_list():
    initial = validate_input(input(f"Type in the first letter of the {data_categories} that you are interested in, then press enter, to see if it's here: "), "initial")
        
    possible_categories = [tag for tag in sorted_categories if tag.startswith(initial)]

    if not possible_categories:
        print(f"There were no {data_categories} matches starting with {initial}. Please try again...")
        return get_category_list()
    
    print(f"There are the following {data_categories} matches starting with the letter {initial}: {', '.join(possible_categories)}")

    user_answer = validate_input(input(f"\nDo you wish to select a {data_categories} from the above list? (Y/N): "), "Y/N")

    if user_answer == "N":
        return get_category_list()
    return get_categories(possible_categories)

def get_categories(possible_categories):
    if len(possible_categories) == 1:
        selected_categories.push(possible_categories[0])
        print(f"Finding recommendations for the {data_categories}: {selected_categories.peek()}")
        return selected_categories
    
    category = validate_input(input(f"Type in the first few letters of the {data_categories} you wish to select from the above list: "), "letters")

    category_match = [tag for tag in possible_categories if tag.startswith(category)]

    if not category_match:
        print(f"There were no {data_categories} matches starting with the letters {category}. Please try again...")
        return get_categories(possible_categories)
    
    if len(category_match) > 1:
        print(f"There were too many matches, please try to type more letters to select a single {data_categories}.")
        return get_categories(possible_categories)
    
    selected_categories.push(category_match[0])
    return selected_categories

def get_recommendations(selected_categories):
    if not selected_categories:
        print("ERROR: NO GENRE SELECTED") # should already be caught by len(genre_match) == 0 in get_genre()
        return

    number_categories = selected_categories.size
    current_category = selected_categories.top_item
    recommendations = []
    category_str = ""
    while current_category:
        current_category_value = current_category.get_value()
        category_str += f"{current_category_value}, "
        if current_category_value in items_in_categories:
            recommendations.extend(items_in_categories[current_category_value])
        current_category = current_category.get_next_node()
    
    sorted_recommendations = sorted(set(item for item in recommendations if recommendations.count(item) == number_categories)) # only get shows that match all genres

    print(f"\nFinding {data_items} recommendations that match the {data_categories} - {category_str[:-2]}:")
    
    if not sorted_recommendations and number_categories > 1:
        last_category = selected_categories.pop()
        print(f"There were no {data_items} recommendations for those {data_categories}. \nRemoving the last {data_categories} added: {last_category}")
        return get_recommendations(selected_categories)
    
    if len(sorted_recommendations) > 5:
        print(f"There are {len(sorted_recommendations)} {data_categories} recommendations for those {data_categories}(s).")
        filter_more = validate_input(input(f"Do you wish to filter recommendations by another {data_categories}? (Y/N): "), "Y/N")

        if filter_more == "N":
            display_recommendations(sorted_recommendations)
            start_again()
        else:
            category_match = get_category_list()
            get_recommendations(category_match)
    else:
        display_recommendations(sorted_recommendations)
        start_again()

def start_again():
    user_answer = validate_input(input("\nDo you wish to start a new recommendation search? (Y/N): "), "Y/N")

    if user_answer == "N":
        exit()
    else:
        genre_match = get_category_list()
        get_recommendations(category_match)

def validate_input(user_answer, input_type):
    user_answer = user_answer.strip().capitalize()

    if input_type == "Y/N":
        while user_answer not in {"Y", "N"}:
            user_answer = input("Please type in Y or N?: ").strip().upper()
    elif input_type == "initial":
        while len(user_answer) != 1 or not user_answer.isalpha():
            user_answer = input("Please type in a single letter: ").strip().upper()
    elif input_type == "letters":
        while not user_answer.isalpha():
            user_answer = input("Please type in letters only: ").strip().capitalize()
    else:
        raise ValueError("ERROR: Invalid input_type specified.")

    return user_answer

def display_recommendations(sorted_recommendations):
    for item in sorted_recommendations:
        print(f"    {item}")
    selected_categories.clear_all()

welcome()
category_match = get_category_list()
get_recommendations(category_match)