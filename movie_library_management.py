import os

def load_movies(filename_parameter):
    pass
    """Loads movies from a CSV file 
and returns them as a list of Movie objects."""
    if not os.path.exists(filename_parameter):
        print("File does not exist.")
    else:
        with open(filename_parameter, 'r') as read_file:
            list_of_all_movies = [line.strip().split(',') for line in read_file]
    return list_of_all_movies
    


def main():
    filename_input = input("Enter the movie catalog filename: ")

    print(load_movies(filename_input))
    


if __name__ == "__main__":
    main()