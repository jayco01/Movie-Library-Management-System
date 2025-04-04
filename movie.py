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
        if self.genre == "0":
            self.genre = "Action"
        if self.genre == "1":
            self.genre = "Comedy"
        if self.genre == "2":
            self.genre = "Drama"
        if self.genre == "3":
            self.genre = "Horror"
        if self.genre == "4":
            self.genre = "Sci-Fi"
        if self.genre == "5":
            self.genre = "Romance"
        if self.genre == "6":
            self.genre = "Thriller"
        if self.genre == "7":
            self.genre = "Animation"
        if self.genre == "8":
            self.genre = "Documentary"
        if self.genre == "9":
            self.genre = "Fantasy"
  

    def get_availability(self):
        if self.available == "True":
            self.available = "Available"
        else:
            self.available = "Rented"


    def borrow_movie(self):
        pass

    def return_movie(self):
        pass

    def __str__(self):
        pass


        