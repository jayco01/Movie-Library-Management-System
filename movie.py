class Movie:
    def __init__(self,id,title,director,genre,available,price,fine_rate=0,rental_count=0):
        self.__id = id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = bool(available)
        self.__price = float(price)
        self.__fine_rate = float(fine_rate)
        self.__rental_count = int(rental_count)
    
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_director(self):
        return self.__director
    
    def get_genre(self):
        return self.__genre
    
    def get_available_boolean(self):
        return self.__available
    
    def get_price(self):
        return self.__price
    
    def get_fine_rate(self):
        return self.__fine_rate
    
    def get_rental_count(self):
        return self.__rental_count
    
    def get_genre_name(self):
        if self.__genre == "0":
            self.__genre = "Action"
        if self.__genre == "1":
            self.__genre = "Comedy"
        if self.__genre == "2":
            self.__genre = "Drama"
        if self.__genre == "3":
            self.__genre = "Horror"
        if self.__genre == "4":
            self.__genre = "Sci-Fi"
        if self.__genre == "5":
            self.__genre = "Romance"
        if self.__genre == "6":
            self.__genre = "Thriller"
        if self.__genre == "7":
            self.__genre = "Animation"
        if self.__genre == "8":
            self.__genre = "Documentary"
        if self.__genre == "9":
            self.__genre = "Fantasy"
  

    def get_availability(self):
        if self.__available == "True":
            self.__available = "Available"
        else:
            self.__available = "Rented"

    def set_id(self, id):
        if isinstance(id, str) and id.strip() != "":
            self.__id = id
        # else:
        #     print("Error! ID must be a valid integer.")

    def set_title(self, title):
        if isinstance(title, str) and title.strip() != "":
            self.__title = title
        # else:
        #     print("Error! Please enter a valid title.")

    def set_director(self, director):
        if isinstance(director, str) and director.strip() != "":
            self.__director = director
        # else:
        #     print("Error! Please enter a valid director.")

    def set_genre(self, genre):
        if isinstance(genre, str) and genre in ["0","1","2","3","4","5","6","7","8","9"]:
            self.__genre = genre
        # else:
        #     print("Error! Please enter a valid genre.")

    def set_price(self, price):
        if isinstance(price, float) and price >= 0:
            self.__price = price
        # else:
        #     print("Error! Please enter a valid price.")

    def borrow_movie(self):
        self.__available = False
        self.__rental_count += 1

    def return_movie(self):
        self.__available = True

    def __str__(self):
        return f"{self.__id:^15}{self.__title:<25}{self.__director:<22}{self.__genre:<11}{self.__available:<18}{self.__price:<12}{self.__rental_count:<19}"