from tv_shows import tv_shows
from classes.stack import Stack

genres = [genre for value in tv_shows.values() for genre in value.split(", ")]
sorted_genres = sorted(list(set(genres)))

selected_genres = Stack()

def welcome():
    print(f"\nWelcome to UK TV shows recommendation software where there are {len(tv_shows)} UK TV shows to choose from!")
    print("Recommendations are chosen from the genre types that you select. So let's get started...\n")

def get_genre_list():
    initial = validate_input(input("Type in the first letter of the genre that you are interested in, then press enter, to see if it's here: "), "initial")
        
    possible_genres = [tag for tag in sorted_genres if tag.startswith(initial)]

    if len(possible_genres) == 0:
        print(f"There were no genre matches starting with {initial}. Please try again...")
        return get_genre_list()
    
    display_possible_genres = f"There are the following genre matches starting with the letter {initial}: {', '.join(possible_genres)}"
    print(display_possible_genres)

    user_answer = validate_input(input("\nDo you wish to select a genre from the above list? (Y/N): "), "Y/N")

    if user_answer == "N":
        return get_genre_list()
    else:
        return get_genre(possible_genres)

def get_genre(possible_genres):
    if len(possible_genres) == 1:
        selected_genres.push(possible_genres[0])
        print(f"Finding recommendations for the genre: {selected_genres.peek()}")
        return selected_genres
    else:
        genre = validate_input(input("Type in the first few letters of the genre you wish to select from the above list: "), "letters")

        genre_match = [tag for tag in possible_genres if tag.startswith(genre)]

        if len(genre_match) == 0:
            print(f"There were no genre matches starting with the letters {genre}. Please try again...")
            return get_genre(possible_genres)
        elif len(genre_match) > 1:
            print("There were too many matches, please try to type more letters to select a single genre.")
            return get_genre(possible_genres)
        else:
            selected_genres.push(genre_match[0])
            return selected_genres

def get_recommendations(selected_genres):
    if selected_genres:
        number_genres = selected_genres.size
        current_genre = selected_genres.top_item
        recommendations = []
        genre_str = ""

        while current_genre is not None:
            current_genre_value = current_genre.get_value()
            genre_str += current_genre_value + ", "
            recommendations += ([key for key, value in tv_shows.items() if current_genre_value in value.split(", ")])
            sorted_recommendations = sorted(list(set(show for show in recommendations if recommendations.count(show) == number_genres))) # only get shows that match all genres
            current_genre = current_genre.get_next_node()

        print(f"\nFinding TV show recommendations that match the genre(s) - {genre_str[:-2]}:")
        if len(sorted_recommendations) == 0 and number_genres > 1:
            last_genre = selected_genres.pop()
            print(f"There were {len(sorted_recommendations)} show recommendations for those genres. \nRemoving the last genre added: {last_genre}")
            return get_recommendations(selected_genres)
        elif len(sorted_recommendations) > 5:
            print(f"There are {len(sorted_recommendations)} show recommendations for those genre(s).")
            filter_more = validate_input(input("Do you wish to filter recommendations by another genre? (Y/N): "), "Y/N")

            if filter_more == "N":
                for show in sorted_recommendations:
                    print(f"    {show}")

                while not selected_genres.is_empty():
                    selected_genres.pop()
                start_again()
            else:
                genre_match = get_genre_list()
                get_recommendations(genre_match)
        else:
            for show in sorted_recommendations:
                print(f"    {show}")

            while not selected_genres.is_empty():
                selected_genres.pop()
            start_again()
    else:
        print("ERROR: NO GENRE SELECTED") # should already be caught by len(genre_match) == 0 in get_genre()

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

welcome()
genre_match = get_genre_list()
get_recommendations(genre_match)