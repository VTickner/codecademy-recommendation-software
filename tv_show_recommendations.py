from tv_shows import tv_shows
from classes.stack import Stack

genres = [genre for value in tv_shows.values() for genre in value.split(", ")]
sorted_genres = sorted(list(set(genres)))

selected_genres = Stack()

def welcome():
    print(f"\nWelcome to UK TV shows recommendation software where there are {len(tv_shows)} UK TV shows to choose from!")
    print("Recommendations are chosen from the genre types that you select. So let's get started...\n")

def get_genre_list():
    initial = input("Type in the first letter of the genre that you are interested in, then press enter, to see if it's here: ").strip()

    while len(initial) != 1 or not initial.isalpha():
        initial = input("Please type in a single letter: ").strip()
        
    possible_genres = [tag for tag in sorted_genres if tag.startswith(initial.upper())]

    if len(possible_genres) == 0:
        print(f"There were no genre matches starting with {initial.upper()}. Please try again...")
        return get_genre_list()
    
    display_possible_genres = f"There are the following genre matches starting with the letter {initial.upper()}: {', '.join(possible_genres)}"
    print(display_possible_genres)

    user_answer = input("\nDo you wish to select a genre from the above list? (Y/N): ").upper()
    while user_answer != "Y" and user_answer != "N":
        user_answer = input("Please type in Y or N?: ").upper()

    if user_answer == "N":
        return get_genre_list()
    elif user_answer == "Y":
        return get_genre(possible_genres)
    else:
        print("ERROR: USER INPUT") # should already be caught by while loop
        return get_genre_list()

def get_genre(possible_genres):
    if len(possible_genres) == 1:
        selected_genres.push(possible_genres[0])
        print(f"Finding recommendations for the genre: {selected_genres.peek()}")
        return selected_genres
    else:
        genre = input("Type in the first few letters of the genre you wish to select from the above list: ").strip()

        while not genre.isalpha():
            genre = input("Please type in letters only: ").strip()

        genre = genre.capitalize()
        genre_match = [tag for tag in possible_genres if tag.startswith(genre)]

        if len(genre_match) == 0:
            print(f"There were no genre matches starting with the letters {genre}. Please try again...")
            return get_genre(possible_genres)
        elif len(genre_match) > 1:
            print("There were too many matches, please try to type more letters to select a single genre.")
            return get_genre(possible_genres)
        else:
            selected_genres.push(genre_match[0])
            print(f"Finding recommendations for the genre: {selected_genres.peek()}")
            return selected_genres

def get_recommendations(selected_genres):
    if selected_genres:
        # TEMP CHECK TO MAKE SURE A GENRE WAS SENT TO FUNCTION
        print(f"In get_recommendations() using genre {selected_genres.peek()}")
    else:
        print("ERROR: NO GENRE SELECTED") # should already be caught by len(genre_match) == 0 in get_genre()

welcome()
genre_match = get_genre_list()
get_recommendations(genre_match)