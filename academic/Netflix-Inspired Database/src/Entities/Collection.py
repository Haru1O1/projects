from Entities.Movie import Movie

class Collection:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def get_name(self):
        return self.name
    
    def get_movies(self):
        return self.movies
    
    def get_total_movies(self):
        return len(self.movies)
    
    def get_total_time(self):
        total = 0
        for movie in self.movies:
            total += movie.get_length()
        
        return total
    
    def list_movies(self):
        self.movies = sorted(self.movies, key=lambda movie: movie.get_title()) 
        for movie in self.movies:
            print("Title: ", movie.get_title())
            print("Age Rating: ", movie.get_agerating())
            print("Length: ", movie.get_length()) 
    
    def set_name(self, name):
        self.name = name
    
    def add_movie(self, title, agerating, length):
        self.movies.append(Movie(title, agerating, length))
    
    def delete_movie(self, title):
        selected_movie = None
        for movie in self.movies:
            if(title.lower() == movie.get_title().lower()):
                selected_movie = movie
        self.movies.remove(selected_movie)
