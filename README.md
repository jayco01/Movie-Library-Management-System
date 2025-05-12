# Movie Rental Manager

## Overview  
This command-line tool lets you manage a small movie‑rental catalogue: search, rent, return, add, remove or update titles, show genre stats and print the top rentals. The program was built for SAIT’s Winter 2025 OOP 1 course and demonstrates class design, encapsulation and file I/O.

## Program Flow (Sample Session)  
A typical run (captured in `output.txt`) works like this:

1. **Startup and catalogue load** – The script asks for a CSV name, loads it into `Movie` objects if found, otherwise starts with an empty list.  
2. **Main loop** – A guarded menu (options 0‑10) repeats until you choose 0. Invalid entries merely reprompt.  
3. **Search (1)** – Prompts for a term and lists any title, director or genre that contains it; otherwise reports no hits.  
4. **Rent (2)** – Given a movie ID, flips its availability flag, increments the rental count and confirms; if not found or already rented, it explains why.  
5. **Return (3)** – Reverses the rent logic, warning if the movie wasn’t out or the ID is missing.  
6. **Add (4)** – Collects a brand‑new ID, title, director, genre and price; rejects duplicates and appends a fresh `Movie`.  
7. **Remove (5)** – Deletes the movie that matches the supplied ID, or notifies you if it can’t.  
8. **Update details (6)** – Lets you press **Enter** to keep existing values while validating any new ones before saving.  
9. **List by genre (7)** – Prints a table of all titles in the chosen genre, or flags bad indexes/empty results.  
10. **Top rented (8)** – Displays the five most‑rented titles via the helper below.  
11. **Availability by genre (9)** – Shows which titles of a given genre are available right now, including a message for none.  
12. **Library summary (10)** – Counts total, available and rented titles and prints the three numbers.  
13. **Exit (0)** – Asks whether to save changes to `movies.csv`, writes if you say yes, then quits.

## Requirements  
* **Python 3.12** or newer  
* Standard library only—no extra setup needed.

## Data File  
`movies.csv` is the live catalogue. Every row holds eight comma‑separated fields—ID, title, director, genre index, availability flag, rental price, fine rate and how many times it has been rented. All changes you make inside the program are written back to this file if you choose to save on exit.

## Key Functions & Algorithms  

### 1  Multi‑field, case‑insensitive search  
```python
def search_movies(list_of_movies_parameter, search_term_parameter):
    """Search movie objects for a term in title, director or genre."""
    movie_objects_list = []
    print(f"Finding ({search_term_parameter}) in title, director, or genre...")
    for movies in list_of_movies_parameter:
        if search_term_parameter.lower() in movies.get_title().lower() or search_term_parameter.lower() in movies.get_director().lower() or search_term_parameter.lower() in movies.get_genre_name().lower():
            movie_objects_list.append(movies)
    if len(movie_objects_list) == 0:
        print("No matching movies found.")
    else:
        label_columns()
        for movie in movie_objects_list:
            print(movie)
```

### 2  Interactive update with validation  
```python
def update_movie_detail(list_of_movies_parameter):
    """Update a movie’s details by ID, keeping any field blank to retain its current value."""
    input_id = input("Enter the movie ID to update: ").strip()
    index = movie_index(list_of_movies_parameter, input_id)

    if index is None:
        print(f"Movie with ID {input_id} is not found.")
        return

    movie = list_of_movies_parameter[index]
    print("Leave fields blank to keep current values.")

    input_title = input(f"Enter new title (current: {movie.get_title()}): ").strip()
    if input_title:
        movie.set_title(input_title)

    input_director = input(f"Enter new director (current: {movie.get_director()}): ").strip()
    if input_director:
        movie.set_director(input_director)

    input_genre = input(f"Enter new genre (current: {movie.get_genre_name()}): ").strip()
    if input_genre:
        if input_genre in Movie.GENRES:
            movie.set_genre(input_genre)
        else:
            print("Invalid genre. Must be a number from 0 to 9.")

    input_price = input(f"Enter new price (current: {movie.get_price()}): ").strip()
    if input_price:
        if input_price.replace('.', '', 1).isdigit():
            movie.set_price(float(input_price))
        else:
            print("Invalid price. Must be a number.")

    print(f"Movie with ID {input_id} is updated successfully.")
```

### 3  Top‑five rental ranking in one expression  
```python
def top_rented_movies(list_of_movies_parameter):
    """Show the five most‑rented titles."""
    top_5 = sorted(
        list_of_movies_parameter,
        key=lambda movie: movie.get_rental_count(),
        reverse=True
    )[:5]
    print("Top 5 Rented Movies:")
    print_movies(top_5)
```

## Testing  
Manual testing is enough: run the script, explore each menu option and compare your results with `output.txt`.

## File Structure  
* `movie.py` – defines the `Movie` class  
* `movie_library_management.py` – main driver, menu loop and persistence  
* `movies.csv` – live catalogue  
* `output.txt` – sample session log

## License  
No licence is attached; use or modify as you wish.

## Quick Start  
Place `movies.csv` in the same folder and run:

```bash
python movie_library_management.py
```

Follow the on‑screen menu to search, rent or update movies and choose whether to save on exit.
