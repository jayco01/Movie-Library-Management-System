class Movie:
    def __init__(self,id,title,director,genre,available,price,fine_rate):
        self.__id = id
        self.__title = title
        self.__director = director
        self.__genre = genre
        self.__available = available
        self.__price = price
        self.__fine_rate = fine_rate
    
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
        if isinstance(id, int) and id.strip() != "":
            self.__id = id
        else:
            print("Error! ID must be a valid integer.")

    def set_title(self, title):
        if isinstance(id, str) and id.strip() != "":
            self.__title = title
        else:
            print("Error! ID must be a valid title.")

    def borrow_movie(self):
        pass

    def return_movie(self):
        pass

    def __str__(self):
        pass


        