from Entities.Collection import Collection
from APIs import DatabaseAPIs
from datetime import datetime

class User: 
    def __init__(self, cursor):
        self.cursor = cursor
        self.API = DatabaseAPIs(cursor)
        self.userid = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.username = None
        self.password = None
        self.creationdate = None
        self.lastaccess = None
        self.collections = []
        self.followers = []
        self.following = []

    def check_credentials(self, username, password=None):
        return self.API.check_credentials(username, password)

    def get_creation_info(self):
        return {
            'lastaccess': self.lastaccess,
            'creationdate': self.creationdate,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        }
    
    def get_userid(self):
        return self.userid
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_email(self):
        return self.email
    
    def get_username(self):
        return self.username
    
    def get_creationdate(self):
        return self.creationdate
    
    def get_lastaccess(self):
        return self.lastaccess
    
    def get_num_collections(self):
        return len(self.collections)
    
    def get_num_following(self):
        return len(self.following)

    def get_num_followers(self):
        return len(self.followers)
    
    def get_top_ten_movies(self, choice):
        if choice == "rating":
            movies = self.API.get_top_ten_movies_by_rating(self.userid)
        elif choice == "most viewed":
            movies = self.API.get_top_ten_movies_by_most_viewed(self.userid)
        else: # Both
            movies = self.API.get_top_ten_movies_by_both(self.userid)

        for movie in movies:
            if(choice == "rating"):
                print("Title: " + str(movie[0]) + ", Rating: " + str(movie[1]))
            elif(choice == "most viewed"):
                print("Title: " + str(movie[0]) + ", Viewed: " + str(movie[1]))
            elif(choice == "both"):
                print("Title: " + str(movie[0]) + ", Rating: " + str(movie[1]) + ", Viewed: " + str(movie[2]))

    def get_top_twenty_in_last_ninety_days(self):
        movies = self.API.get_top_twenty_in_last_ninety_days()
        
        for movie in movies:
            print("Title: " + movie[0] + ", People Watched This: " + str(movie[1]) + " times")

    def get_top_twenty_movies_among_followers(self):
        movies = self.API.get_top_twenty_movies_among_followers(self.userid)

        for movie in movies:
            print("Title: " + movie[0] + ", Your Followers Played This: " + str(movie[1]) + " times")

    def get_top_five_new_releases(self):
        movies = self.API.get_top_five_new_releases(datetime.now())
        
        for movie in movies:
            print("Title:", movie)

    def get_recommendations(self):
        movies, genre_type, actor_name = self.API.get_recommendations(self.userid, "genre")
        
        print("\nRecommendations for you based top viewed movies of your favorite genre ", genre_type, " or your favorite actor ", actor_name, ".", sep="")
        for movie in movies:
            print("Title:", movie[0])

    def list_collections(self):
        self.collections = sorted(self.collections, key=lambda collection: collection.name)
        for collection in self.collections:
            print("Collection: ", collection.get_name())
            print("Total Movies: ", collection.get_total_movies())
            time = collection.get_total_time()
            print("Total Time: " + str(time // 60) + ":" + str(time % 60) + "\n")
    
    def list_movies_in_collection(self, name):
        for collection in self.collections:
            if(name == collection.get_name()):
                collection.list_movies()
                break
    
    def add_account(self, firstname, lastname, email, username, password, creationdate):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
        self.creationdate = creationdate

        self.API.add_user(self.get_creation_info())
        self.userid = self.API.get_userid(self.username)
    
    def create_collection(self, name):
        self.collections.append(Collection(name))
        self.API.add_collection(self.userid, name)

    def change_collection_name(self, current_name, new_name):
        selected_collection = None

        for collection in self.collections:
            if current_name == collection.get_name():
                selected_collection = collection
        
        selected_collection.set_name(new_name)
        self.API.update_collection_name(self.userid, current_name, new_name)

    def add_to_collection(self, name, title):
        selected_collection = None

        for collection in self.collections:
            if name == collection.get_name():
                selected_collection = collection
                #print(selected_collection)
        
        id = self.API.get_movid(title)
        #print("id is", id)
        movie = self.API.get_movie(id)
        #print("movie is", movie)
        selected_collection.add_movie(movie[0], movie[1], movie[2]) # title, agerating, length
        self.API.add_movie_to_collection(selected_collection.get_name(), title)

    def play_collection(self, name):
        selected_collection = None

        for collection in self.collections:
            if name == collection.get_name():
                selected_collection = collection
        
        for movie in selected_collection.get_movies():
            print("Playing " + movie.get_title() + "...")
            self.play_movie(movie.get_title())
            print("Finished playing " + movie.get_title() + "!")

    def play_movie(self, title):
        time = datetime.now()
        self.API.add_record(self.userid, title, time)

    def rate_movie(self, title, rating):
        self.API.add_rating(self.userid, title, rating)

    def set_userid(self, userid):
        self.userid = userid

    def update_all_info(self, userid, lastaccess, creationdate, username, password, email, firstname, lastname):
        self.userid = userid
        self.lastaccess = lastaccess
        self.creationdate = creationdate
        self.username = username
        self.password = password
        self.email = email
        self.firstname = firstname
        self.lastname = lastname

        collections = self.API.get_existing_collections(self.userid)
        followers = self.API.get_followers(self.userid)
        following = self.API.get_following(self.userid)

        if collections is not None:
            index = 0
            # Populate local collection
            for collection in collections:
                self.collections.append(Collection(collection['name']))
                selected_collection = self.collections[index]
                
                for movie in collection['movies']:
                    selected_collection.add_movie(movie['title'], movie['agerating'], movie['length'])
                
                index+=1

        if followers is not None:
            for follower in followers:
                self.followers.append(follower)
        
        if following is not None:
            for follow in following:
                self.following.append(follow)


    def update_creationdate(self, creationdate):
        self.creationdate = creationdate

    def update_lastaccess(self, lastaccess):
        self.lastaccess = lastaccess
        self.API.update_lastaccess(self.userid, self.lastaccess)

    def delete_from_collection(self, name, title):
        selected_collection = None

        for collection in self.collections:
            if name == collection.get_name():
                selected_collection = collection
        
        id = self.API.get_movid(title)
        movie = self.API.get_movie(id)
        selected_collection.delete_movie(movie[0])
        self.API.delete_movie_from_collection(selected_collection.get_name(), title)

    def delete_collection(self, name):
        selected_collection = None
        for collection in self.collections:
            if(name.lower() == collection.get_name().lower()):
                selected_collection = collection
            
        self.collections.remove(selected_collection)
        self.API.delete_collection(self.userid, name)

    def check_user(self, user_mail):
        return self.API.check_user(user_mail)

    def follow_user(self, friend_id):
        return self.API.follow_user(self.userid, friend_id)

    def unfollow_user(self, friend_id):
        return self.API.unfollow_user(self.userid, friend_id)

    def search_movie(self, choice, search):
        if(choice == "1"):
            search_param = "Name"
            results = self.API.search_by_name(search)
        elif(choice == "2"):
            search_param = "Release Date"
            results = self.API.search_by_release_date(search)
        elif(choice == "3"):
            search_param = "Cast Member"
            results = self.API.search_by_cast(search)
        elif(choice == "4"):
            search_param = "Studio"
            results = self.API.search_by_studio(search)
        elif(choice == "5"):
            search_param = "Genre"
            results = self.API.search_by_genre(search)

        if(results is not None):
            print("\nSearch Results (by " + search_param + "):")
            for result in results:
                title, length, age_rating, user_rating, cast_members, directors, genre = result
                print("Title:", title)
                print("Length:", length)
                print("Age Rating:", age_rating)
                print("User Rating:", user_rating)
                print("Cast Members:", cast_members)
                print("Directors:", directors)
                print("Genre: ", genre)
                print()
            return results
        else:
            print("\nNo movies found for the given " + search_param.lower() + ".")
            return None
        
    def sort_movies(self, results, sort_choice, up_or_down):
        if(sort_choice == "1"):  # Sort by name
            search = "Name"
            results.sort(key=lambda x: x[0], reverse=(up_or_down == "d"))
        elif(sort_choice == "2"):  # Sort by release date
            search = "Release Date"
            results.sort(key=lambda x: x[1], reverse=(up_or_down == "d"))
        elif(sort_choice == "3"):  # Sort by studio
            search = "Studio"
            results.sort(key=lambda x: x[5], reverse=(up_or_down == "d"))
        elif(sort_choice == "4"):  # Sort by genre
            search = "Genre"
            results.sort(key=lambda x: x[6], reverse=(up_or_down == "d"))
        
        print("\nSearch Results (by " + search + "):")
        for result in results:
            title, length, age_rating, user_rating, cast_members, directors, genre = result
            print("Title:", title)
            print("Length:", length)
            print("Age Rating:", age_rating)
            print("User Rating:", user_rating)
            print("Cast Members:", cast_members)
            print("Directors:", directors)
            print("Genre: ", genre)
            print()

