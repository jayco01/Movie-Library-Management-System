from movie import Movie
import os


def load_movies(filename_parameter):
    """Loads movies from a CSV file 
and returns them as a list of Movie objects."""
    if not os.path.exists(filename_parameter):
         return print(f"The catalog file {filename_parameter} is not found\nThe movie library management system starts without catalog")
    else:
        with open(filename_parameter, 'r') as read_file:
            list_of_all_movies = [line.strip().split(',') for line in read_file]
        movie_objects = []
        for movie in list_of_all_movies:
            movie_instance = Movie(*movie)
            movie_objects.append(movie_instance)
        return movie_objects


def save_movies(filename_parameter, movie_objects_list_parameter):
    """Saves the list of Movie objects 
to a CSV file."""
    with open(filename_parameter, "w") as write_file:
        for movie in movie_objects_list_parameter:
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


def search_movies(list_of_movies_parameter, search_term_parameter):
    movie_objects_list = []
    for movies in list_of_movies_parameter:
        if search_term_parameter.lower() in movies[1].lower() or search_term_parameter.lower() in movies[2].lower() or search_term_parameter.lower() in movies[3].lower():
            movie_objects_list.append(movies)
    return movie_objects_list


def rent_movie(list_of_movies_parameter, movie_id_parameter): # I might have to add a functionality to update movie status as the movie is being rented
    """Description: Rents a movie by its ID if it is 
available. 
"""
    id_found = False
    for movie in list_of_movies_parameter:
        if movie.get_id() == movie_id_parameter and movie.get_available_boolean() == True:
            id_found = True
            movie.borrow_movie()
            return f"You have successfully rented '{movie.get_title()}'."
        elif movie.get_id() == movie_id_parameter and movie.get_available_boolean() == False:
            id_found = True
            return f"'Movie{movie.get_id()}' is already rented."
    if id_found == False:
        return f"Movie with ID {movie_id_parameter} not found."


def main():
    filename_input = input("Enter the movie catalog filename: ")

    list_of_movie_objects = load_movies(filename_input)

    print()
    selected = print_menu()


    # if :
    # elif selected == "0":

    

if __name__ == "__main__":
    main()