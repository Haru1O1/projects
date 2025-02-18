class Movie:
    def __init__(self, title, agerating, length):
        self.title = title
        self.agerating = agerating
        self.length = length
        self.rating = 0

    def get_title(self):
        return self.title
    
    def get_agerating(self):
        return self.agerating
    
    def get_length(self):
        return self.length
    
    def get_rating(self):
        return self.rating
