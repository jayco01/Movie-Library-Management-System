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
    print(f"Finding ({search_term_parameter}) in title, director, or genre...")
    for movies in list_of_movies_parameter:
        if search_term_parameter.lower() in movies.get_title().lower() or search_term_parameter.lower() in movies.get_director().lower() or search_term_parameter.lower() in movies.get_genre_name().lower():
            movie_objects_list.append(movies)
    if len(movie_objects_list) == 0:
        "No matching movies found."
    else:
        for movie in movie_objects_list:
            print(movie)


def rent_movie(list_of_movies_parameter, movie_id_parameter):
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
            return f"'{movie.get_id()}' is already rented."
    if id_found == False:
        return f"Movie with ID {movie_id_parameter} not found."

def return_movie(list_of_movies_parameter, movie_id_parameter):
    """Returns a rented movie by its 
ID."""
    id_found = False
    for movie in list_of_movies_parameter:
        if movie.get_id() == movie_id_parameter and movie.get_available_boolean() == False:
            id_found = True
            movie.return_movie()
            return f"You have successfully returned '{movie.get_title()}'."
        elif movie.get_id() == movie_id_parameter and movie.get_available_boolean() == True:
            id_found = True
            return f"'{movie.get_title()}' was not rented."
    if id_found == False:
        return f"Movie with ID {movie_id_parameter} not found." 


def add_movie(list_of_movies_parameter):
    """Adds a new movie to the library 
after prompting the user for details. """
    input_id = input("Enter movie ID: ")
    id_found = False
    for movie in list_of_movies_parameter:
        if movie.get_id() == input_id:
            id_found = True
            print(f"Movie with ID {input_id} exists")
            break
    
    if id_found == False:
        input_title = input("Enter title: ")
        input_director = input("Enter director: ")
        input_genre = input("Enter genre (0-9): ")
        input_price = input("Enter price: ")
        new_movie = Movie(input_id,input_title,input_director,input_genre,True,input_price)
        list_of_movies_parameter.append(new_movie)
        print(f"Movie '{input_title}' added successfully. ")

def remove_movie(list_of_movies_parameter):
    """Removes a movie from the 
library by its ID. Displays a message 
confirming that the movie is removed, or the 
movie is not found."""
    input_id = input("Enter your selection: ")
    id_found = False
    for movie in list_of_movies_parameter:
        if movie.get_id() == input_id:
            id_found = True
            list_of_movies_parameter.remove(movie)
            print(f"Movie '{movie.get_title()}' has been removed.")
            break
    if id_found == False:
        print(f"Movie with ID {input_id} not found.")


def update_movie_detail(list_of_movies_parameter):
    """Updates the details of a movie 
by its ID. Displays a message confirming 
that the movie is updated, or the movie is 
not found."""
    input_id = input("Enter your selection: ")
    id_found = False
    for movie in list_of_movies_parameter:
        if movie.get_id() == input_id:
            id_found = True
            print("Leave fields blank to keep current values.")
            input_title = input(f"Enter new title (current: {movie.get_title()}): ")
            if input_title.strip() != "":
                movie.set_title(input_title.strip())

            input_director = input(f"Enter new director (current: {movie.get_director()}): ")
            if input_director.strip() != "":
                movie.set_director(input_director.strip())

            input_genre = input(f"Enter new genre (current: {movie.get_genre()}): ")
            if input_genre.strip() != "":
                movie.set_genre(input_genre.strip())

            input_price = input(f"Enter new price (current: {movie.get_price()}): ")
            if input_price.strip() != "":
                movie.set_price(float(input_price.strip()))

            print(f"Movie with ID {input_id}' is updated successfully.")
            break
            
    if id_found == False:
        print(f"Movie with ID {input_id} is not found.")


def list_movies_by_genre(list_of_movies_parameter):
    """Lists all movies of a specified genre. Displays a list of movies in the specified genre, no movies found, or invalid genre."""
    genre_found = False
    found_movies = []

    selected_genre = input("Enter genre (0-9): ")
    if int(selected_genre) < 0 or int(selected_genre) > 9:
        print("Invalid Genre: Enter a valid genre (0-9)")
    for movie in list_of_movies_parameter:
        if movie.get_genre() == selected_genre:
            genre_found = True
            found_movies.append(movie)
    
    if genre_found:
        for movie in found_movies:
            print(movie)
    else:
        print(f'There are no movies found for the selected genre.')


def check_availability_by_genre(list_of_movies_parameter):
    """Checks and displays the availability of movies in a specified genre. Displays a list of movies that are available"""

    genre_found = False
    available = False
    found_movies = []

    selected_genre = input("Enter genre (0-9): ")

    if int(selected_genre) < 0 or int(selected_genre) > 9:
        print("Invalid Genre: Enter a valid genre (0-9)")
    for movie in list_of_movies_parameter:
        if movie.get_genre() == selected_genre and movie.get_available_boolean() == True:
            genre_found = True
            available= True
            found_movies.append(movie)
        elif movie.get_genre() == selected_genre and movie.get_available_boolean() == False:
            genre_found = True
    
    if genre_found and available:
        for movie in found_movies:
            print(movie)
    elif genre_found and available == False:
        print("There are no movies availalbe for the {selected_genre} genre.")
    else:
        print('There are no movies found for the {selected_genre} genre.')


def diplay_library_summary(list_of_movies_parameter):
    """Displays a summary of the library, including the total number of movies, number of available movies, and number of rented movies."""
    total_movies = 0
    available_movies = 0
    rented_movies = 0

    for movie in list_of_movies_parameter:
        total_movies += 1
        if movie.get_available_boolean() == True:
            available_movies += 1
        else:
            rented_movies += 1

    print(f"Total movies: {total_movies}")
    print(f"Available movies: {available_movies}")
    print(f"Rented movies: {rented_movies}")


def top_rented_movies(list_of_movies_parameter):
    """Displays the top 5 most rented movies based on their rental count."""
    top_5 = sorted(list_of_movies_parameter, key=lambda movie: movie.get_rental_count())
    print("Top 5 Rented Movies:")
    print_movies(top_5)


def print_movies(list_of_movies_parameter):
    """Helper function to find the index of a movie by its ID."""
    print(f"{"ID":<11}{"Title":<26}{"Director":<21}{"Genre":<17}{"Rentals":<8}")
    print("-"*83)
    for movie in list_of_movies_parameter:
        print(f"{movie.get_id():<11}{movie.get_title():<26}{movie.get_director():<21}{movie.get_genre():<17}{movie.get_rental_count():<8}")


def movie_index(list_of_movies_parameter, movie_id_parameter):
    """Helper function to find the index of a movie by its ID."""
    index = 0
    for movie in list_of_movies_parameter:
        index += 1
        if movie.get_id() == movie_id_parameter:
            break
    if index > 0:
        return index
    else:
        return None

def main():
    filename_input = input("Enter the movie catalog filename: ")

    list_of_movie_objects = load_movies(filename_input)

    print()
    selected = None
    while selected != 0:
        selected = int(print_menu())
        if selected == 1:
            search_term = input("Enter search term: ").strip()
            print(search_movies(list_of_movie_objects, search_term))
        if selected == 2:
            rent_movie_selected = input("Enter the movie ID to rent: ")
            rent_movie(list_of_movie_objects,rent_movie_selected)
        
        if selected == 3:
            return_movie_selected = input("Enter the movie ID to return: ")
            return_movie(list_of_movie_objects,return_movie_selected)
            
        if selected == 10:
            diplay_library_summary(list_of_movie_objects)

    

if __name__ == "__main__":
    main()