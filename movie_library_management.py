import os

def load_movies(filename_parameter):
    """Loads movies from a CSV file 
and returns them as a list of Movie objects."""
    if not os.path.exists(filename_parameter):
         return print(f"The catalog file (movies) is not found\nThe movie library management system starts without catalog")
    else:
        with open(filename_parameter, 'r') as read_file:
            list_of_all_movies = [line.strip().split(',') for line in read_file]
        return list_of_all_movies
    

def save_movies(filename_parameter, movies_parameter):
    """Saves the list of Movie objects 
to a CSV file."""
    pass


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

    selected = input("Enter your selection: ")

    return selected




def main():
    filename_input = input("Enter the movie catalog filename: ")

    load_movies(filename_input)

    print()
    print_menu()
    
    


if __name__ == "__main__":
    main()