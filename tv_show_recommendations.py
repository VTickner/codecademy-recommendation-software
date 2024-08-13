import json
from classes.stack import Stack

def load_transformed_dict(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)
    
shows_in_genres = load_transformed_dict("data.json")
genres = [genre for genre in shows_in_genres.keys()]
sorted_genres = sorted(set(genres))
selected_genres = Stack()

def welcome():
    number_shows = len(set([show for shows in shows_in_genres.values() for show in shows]))
    print(f"\nWelcome to UK TV shows recommendation software where there are {number_shows} UK TV shows to choose from!")
    print("Recommendations are chosen from the genre types that you select. So let's get started...\n")

def get_genre_list():
    initial = validate_input(input("Type in the first letter of the genre that you are interested in, then press enter, to see if it's here: "), "initial")
        
    possible_genres = [tag for tag in sorted_genres if tag.startswith(initial)]

    if not possible_genres:
        print(f"There were no genre matches starting with {initial}. Please try again...")
        return get_genre_list()
    
    print(f"There are the following genre matches starting with the letter {initial}: {', '.join(possible_genres)}")

    user_answer = validate_input(input("\nDo you wish to select a genre from the above list? (Y/N): "), "Y/N")

    if user_answer == "N":
        return get_genre_list()
    return get_genre(possible_genres)

def get_genre(possible_genres):
    if len(possible_genres) == 1:
        selected_genres.push(possible_genres[0])
        print(f"Finding recommendations for the genre: {selected_genres.peek()}")
        return selected_genres
    
    genre = validate_input(input("Type in the first few letters of the genre you wish to select from the above list: "), "letters")

    genre_match = [tag for tag in possible_genres if tag.startswith(genre)]

    if not genre_match:
        print(f"There were no genre matches starting with the letters {genre}. Please try again...")
        return get_genre(possible_genres)
    
    if len(genre_match) > 1:
        print("There were too many matches, please try to type more letters to select a single genre.")
        return get_genre(possible_genres)
    
    selected_genres.push(genre_match[0])
    return selected_genres

def get_recommendations(selected_genres):
    if not selected_genres:
        print("ERROR: NO GENRE SELECTED") # should already be caught by len(genre_match) == 0 in get_genre()
        return

    number_genres = selected_genres.size
    current_genre = selected_genres.top_item
    recommendations = []
    genre_str = ""

    while current_genre:
        current_genre_value = current_genre.get_value()
        genre_str += f"{current_genre_value}, "
        if current_genre_value in shows_in_genres:
            recommendations.extend(shows_in_genres[current_genre_value])
        current_genre = current_genre.get_next_node()
    
    sorted_recommendations = sorted(set(show for show in recommendations if recommendations.count(show) == number_genres)) # only get shows that match all genres

    print(f"\nFinding TV show recommendations that match the genre(s) - {genre_str[:-2]}:")
    
    if not sorted_recommendations and number_genres > 1:
        last_genre = selected_genres.pop()
        print(f"There were no show recommendations for those genres. \nRemoving the last genre added: {last_genre}")
        return get_recommendations(selected_genres)
    
    if len(sorted_recommendations) > 5:
        print(f"There are {len(sorted_recommendations)} show recommendations for those genre(s).")
        filter_more = validate_input(input("Do you wish to filter recommendations by another genre? (Y/N): "), "Y/N")

        if filter_more == "N":
            display_recommendations(sorted_recommendations)
            start_again()
        else:
            genre_match = get_genre_list()
            get_recommendations(genre_match)
    else:
        display_recommendations(sorted_recommendations)
        start_again()

def start_again():
    user_answer = validate_input(input("\nDo you wish to start a new recommendation search? (Y/N): "), "Y/N")

    if user_answer == "N":
        exit()
    else:
        genre_match = get_genre_list()
        get_recommendations(genre_match)

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
    for show in sorted_recommendations:
        print(f"    {show}")
    selected_genres.clear_all()

welcome()
genre_match = get_genre_list()
get_recommendations(genre_match)