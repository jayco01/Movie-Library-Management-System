from movie import Movie
import os


def create_movie_objects(list_of_movies_parameter):
    movie_objects = []
    for movie in list_of_movies_parameter:
        movie_instance = Movie(*movie)
        movie_objects.append(movie_instance)
    return movie_objects


def load_movies(filename_parameter):
    """Loads movies from a CSV file 
and returns them as a list of Movie objects."""
    if not os.path.exists(filename_parameter):
         return print(f"The catalog file {filename_parameter} is not found\nThe movie library management system starts without catalog")
    else:
        with open(filename_parameter, 'r') as read_file:
            list_of_all_movies = [line.strip().split(',') for line in read_file]
        return list_of_all_movies
    

def save_movies(filename_parameter, list_of_movies_parameter):
    """Saves the list of Movie objects 
to a CSV file."""
    with open(filename_parameter, "w") as write_file:
        for movie in list_of_movies_parameter:
            write_file.write(",".join(movie) + "\n")


def print_menu():
    """Displays the main menu and 
prompts the user for a valid choice."""
    print("Movie Library - Main Menu")
    print("="*25)
    print("1) Search for movies")
    print("2) Rent a movie ")
    print("3) Return a movie")
    print("4) Add a movie")
    print("5) Remove a movie")
    print("6) Update movie details")
    print("7) List movies by genre")
    print("8) Top rented movies")
    print("9) Check availability by genre")
    print("10) Display library summary")
    print("0) Exit the system")
    list_of_options = ["1","2","3","4","5","6","7","8","9","10","0"]
    selected = input("Enter your selection: ")
    while selected not in (list_of_options):
        print("Invalid choice. Please try again.")
        selected = input("Enter your selection: ")

    return selected


# def search_movies(list_of_movies_parameter, search_term_parameter):
#     for search_term ==
#         if search_term_parameter == 


# def search_movies(list_of_movies_parameter, search_term_parameter):
#     movie_found = False

#     for 

# def update_movie_details(list_of_movies_parameter):
#     with open () 


def main():
    filename_input = input("Enter the movie catalog filename: ")

    list_of_all_movies = load_movies(filename_input)

    print()
    selected = print_menu()

    print(list_of_all_movies)

    # if :
    # elif selected == "0":

    

if __name__ == "__main__":
    main()