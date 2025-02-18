class DatabaseAPIs:
    def __init__(self, cursor):
        self.cursor = cursor

    """
    Check database for valid credentials
    """
    def check_credentials(self, username, password):
        if(password == None):
            query = "SELECT COUNT(*) FROM users WHERE username = %s"
            self.cursor.execute(query, (username,))
            count = self.cursor.fetchone()[0]
            return count > 0
        else:
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password,))
            result = self.cursor.fetchone()

            if result is not None:
                return {
                    'userid' : result[0],
                    'lastaccess': result[1],
                    'creationdate': result[2],
                    'username': result[3],
                    'password': result[4],
                    'email': result[5],
                    'firstname': result[6],
                    'lastname': result[7]
                }
            else:
                return None
    """
    Gets userid given a username
    """
    def get_userid(self, username):
        query = "SELECT userid FROM users WHERE username = %s"

        try:
            self.cursor.execute(query, (username,))
            userid = self.cursor.fetchone()
            if userid:
                return userid[0]  # Get userid from tuple
            else:
                return None
        except Exception as e:
            print("Error retrieving userid:", e)
            return None
    
    """
    Gets all collections for a user
    """
    def get_existing_collections(self, userid):
        full_collections = [] # Contains list of collection
        query = "SELECT name FROM collection where userid = %s"

        self.cursor.execute(query, (userid,))
        result = self.cursor.fetchall()

        if result:
            for coll in result:
                collection = {'name': coll[0], 'movies': []}
                full_collections.append(collection)
            
            query = "SELECT movid FROM collectionofmovies WHERE name = %s"
            for coll in full_collections:
                self.cursor.execute(query, (coll['name'],))
                result = self.cursor.fetchall()

                if result:
                    for id in result:
                        info = self.get_movie(id[0])
                        movie = {'title': info[0], 'agerating': info[1], 'length': info[2]}
                        coll['movies'].append(movie)
                        
        return full_collections

    """
    Check if user exists
    """
    def check_user(self, user_mail):
        query = "SELECT userid FROM users where email = %s"

        try:
            self.cursor.execute(query, (user_mail,))
            user = self.cursor.fetchone()
            if user:
                return user
            else:
                return None
        except Exception as e:
            print("Error retrieving user:", e)
            return None

    
    """
    Gets movid
    """
    def get_movid(self, movname):
        #print("print movie name", movname)
        query = "SELECT movid FROM movies WHERE title ILIKE %s"
        
        try:
            self.cursor.execute(query, (movname,))
            movid = self.cursor.fetchone()
            if movid:
                return movid[0]
            else:
                return None
        except Exception as e:
            print("Error retrieving movid:", e)
            return None

    """
    Gets movie information
    """
    def get_movie(self, movid):
        query = "SELECT title, agerating, length FROM movies where movid = %s"

        try:
            self.cursor.execute(query, (movid,))
            movie = self.cursor.fetchone()
            if movie:
                return movie
            else:
                return None
        except Exception as e:
            print("Error retrieving movie:", e)
            return None
        
    """
    Gets user's followers
    """
    def get_followers(self, userid):
        query = "SELECT userid1 FROM friend where userid2 = %s"

        try:
            self.cursor.execute(query, (userid,))
            followers = self.cursor.fetchall()
            if followers:
                return followers
            else:
                return None
        except Exception as e:
            print("Error retrieving followers:", e)
            return None

    """
    Gets user's following
    """
    def get_following(self, userid):
        query = "SELECT userid2 FROM friend where userid1 = %s"

        try:
            self.cursor.execute(query, (userid,))
            followers = self.cursor.fetchall()
            if followers:
                return followers
            else:
                return None
        except Exception as e:
            print("Error retrieving following:", e)
            return None
        
    """
    Get user's top ten movies by rating
    """
    def get_top_ten_movies_by_rating(self, userid):
        query = """
                SELECT m.title, r.userrating
                FROM movies m
                JOIN rating r ON m.movID = r.movID
                WHERE r.userid = %s
                ORDER BY r.userrating DESC
                LIMIT 10
                """
        try:
            self.cursor.execute(query, (userid,))
            top_movies = self.cursor.fetchall()
            if top_movies:  
                return top_movies
            else:
                return None
        except Exception as e:
            print("Error retrieving top movies by rating:", e)
            return None
        
    """
    Get user's top ten movies by most viewed
    """
    def get_top_ten_movies_by_most_viewed(self, userid):
        query = """
                SELECT m.title, COUNT(r.movid) AS views
                FROM movies m
                JOIN record r ON m.movID = r.movID
                WHERE r.userid = %s
                GROUP BY m.title
                ORDER BY views DESC
                LIMIT 10
                """

        try:
            self.cursor.execute(query, (userid,))
            top_movies = self.cursor.fetchall()
            if top_movies:
                return top_movies
            else: 
                return None
            
        except Exception as e:
            print("Error retrieving top movies by viewed:", e)
            return None
        
    """
    Gets user's top ten movies using both ratings and views
    """
    def get_top_ten_movies_by_both(self, userid):
        top_movies_by_rating = self.get_top_ten_movies_by_rating(userid)
        top_movies_by_views = self.get_top_ten_movies_by_most_viewed(userid)

        if top_movies_by_rating is None and top_movies_by_views is None:
            return None
        elif top_movies_by_rating is None:
            return top_movies_by_views
        elif top_movies_by_views is None:
            return top_movies_by_rating
        
        combined_top_movies = []

        for movie_rating in top_movies_by_rating:
            for movie_views in top_movies_by_views:
                if movie_rating[0] == movie_views[0]:
                    combined_top_movies.append((movie_rating[0], movie_rating[1], movie_views[1]))
                    break

        return combined_top_movies[:10]  # Return only top 10
    
    """
    Get top 20 movies in the last 90 days
    """
    def get_top_twenty_in_last_ninety_days(self):
        query = """
            SELECT m.title, COUNT(r.movid) AS play_count
            FROM movies m
            JOIN record r ON m.movID = r.movID
            WHERE r.timestamp >= NOW() - INTERVAL '90 days'
            GROUP BY m.title
            ORDER BY play_count DESC
            LIMIT 20
        """

        try:
            self.cursor.execute(query)
            top_twenty = self.cursor.fetchall()
            if top_twenty:
                return top_twenty
            else:
                return None
        except Exception as e:
            print("Error retrieving top twenty popular movies in the last ninety days:", e)
            return None
        
    """
    Gets top twenty movies among the user's followers
    """
    def get_top_twenty_movies_among_followers(self, userid):
        query = """
            SELECT m.title, COUNT(r.movid) AS play_count
            FROM movies m
            JOIN record r ON m.movID = r.movID
            JOIN friend f ON r.userid = f.userid2
            WHERE f.userid1 = %s
            GROUP BY m.title
            ORDER BY play_count DESC
            LIMIT 20
        """

        try:
            self.cursor.execute(query, (userid,))
            top_twenty = self.cursor.fetchall()
            if top_twenty:
                return top_twenty
            else:
                return None
        except Exception as e:
            print("Error retrieving top twenty popular movies among followers:", e)
            return None
    
    """
    Get top five movies in this month
    """
    def get_top_five_new_releases(self, current_date):
        current_month = current_date.month
        current_year = current_date.year

        query = """
            SELECT m.title
            FROM movies m
            JOIN releasing r ON m.movID = r.movID
            WHERE EXTRACT(MONTH FROM r.releasedate) = %s
            AND EXTRACT(YEAR FROM r.releasedate) = %s
            ORDER BY r.releasedate DESC
            LIMIT 5
        """
        try:
            self.cursor.execute(query, (current_month, current_year))
            top_new_releases = self.cursor.fetchall()
            return [movie[0] for movie in top_new_releases]  # Extracting titles from the result set
        except Exception as e:
            print("Error retrieving top new release titles:", e)
            return None

    def get_favorite_genre(self, userid):
        query = """
                SELECT g.genretype, gm.genreid
                FROM movies m
                JOIN movieshasgenre gm ON m.movid = gm.movID
                JOIN record r ON m.movID = r.movID
                JOIN genre g ON gm.genreid = g.genreid
                WHERE r.userid = %s
                GROUP BY g.genretype, gm.genreid
                ORDER BY COUNT(gm.genreid) DESC
                LIMIT 1
                """
        try:
            self.cursor.execute(query, (userid,))
            top_genre = self.cursor.fetchall()
            if top_genre:
                return top_genre
            else:
                return None

        except Exception as e:
            print("Error retrieving top genre by viewed:", e)
            return None

    def get_favorite_actor(self, userid):
        query = """
                SELECT c.name AS actor_name, a.id AS actor_id
                FROM movies m
                JOIN record r ON m.movID = r.movID
                JOIN acts_in a ON m.movid = a.movid
                JOIN contributors c ON a.id = c.id
                WHERE r.userid = %s
                GROUP BY actor_name, actor_id
                ORDER BY COUNT(r.movID) DESC
                LIMIT 1
                """
        try:
            self.cursor.execute(query, (userid,))
            top_actor = self.cursor.fetchall()
            if top_actor:
                return top_actor
            else:
                return None

        except Exception as e:
            print("Error retrieving favorite actor by viewed:", e)
            return None

    def get_recommendations(self, userid, option):
        top_genre = self.get_favorite_genre(userid)
        top_actor = self.get_favorite_actor(userid)
        query = """
                SELECT DISTINCT m.title
                FROM movies m
                JOIN record r ON m.movID = r.movID
                JOIN movieshasgenre gm ON m.movid = gm.movid
                JOIN acts_in a ON m.movid = a.movid
                WHERE r.timestamp >= NOW() - INTERVAL '90 days' AND (gm.genreid = %s OR a.id = %s)
                GROUP BY m.title
                ORDER BY m.title DESC
                LIMIT 10
                """
        try:
            self.cursor.execute(query, (top_genre[0][1], top_actor[0][1]))
            top_movies = self.cursor.fetchall()
            if top_movies:
                return top_movies, top_genre[0][0], top_actor[0][0]
            else:
                return None

        except Exception as e:
            print("Error retrieving recommendations:", e)
            return None

    """
    Insert new account credentials into Users
    """
    def add_user(self, user_data):
        query = "INSERT INTO users (lastaccess, creationdate, username, password, email, firstname, lastname) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(query, (
                user_data['lastaccess'],
                user_data['creationdate'],
                user_data['username'],
                user_data['password'],
                user_data['email'],
                user_data['firstname'],
                user_data['lastname']
            ))
            # Commit transaction to apply changes to database
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error adding user:", e)
            # Rollback when error
            self.cursor.connection.rollback()
            return False
        
    """
    Inserts new collection
    """
    def add_collection(self, userid, name):
        query = "INSERT INTO collection (name, userid) VALUES (%s, %s)"
        try:
            self.cursor.execute(query, (name, userid))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error adding collection:",  e)
            self.cursor.connection.rollback()
            return False
        
    """
    Inserts movie into existing collection
    """
    def add_movie_to_collection(self, coll_name, movname):
        movid = self.get_movid(movname)
        query = "INSERT INTO collectionofmovies (name, movid) VALUES (%s, %s)"
        
        try:
            self.cursor.execute(query, (coll_name, movid))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error adding movie to collection:",  e)
            self.cursor.connection.rollback()
            return False
        
    """
    Adds record of when movie was played
    """
    def add_record(self, userid, movname, time):
        movid = self.get_movid(movname)
        query = "INSERT INTO record (userid, movid, timestamp) VALUES (%s, %s, %s)"

        try:
            self.cursor.execute(query, (userid, movid, time))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error adding time to record:",  e)
            self.cursor.connection.rollback()
            return False
    
    """
    Adds user's rating to database
    """
    def add_rating(self, userid, movname, rating):
        movid = self.get_movid(movname)
        query = "INSERT INTO rating (userid, movid, userrating) VALUES (%s, %s, %s)"

        try:
            self.cursor.execute(query, (userid, movid, rating))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error adding user's rating:",  e)
            self.cursor.connection.rollback()
            return False
    
    """
    Updates lastaccess of user, use when user logs in
    """
    def update_lastaccess(self, userid, lastaccess):
        query = "UPDATE users SET lastaccess = %s WHERE userid = %s"

        try:
            self.cursor.execute(query, (lastaccess, userid))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error updating last access:", e)
            self.cursor.connection.rollback()
            return False
        
    """
    Updates name of a user's collection
    """
    def update_collection_name(self, userid, current_name, new_name):
        query = "UPDATE collection SET name = %s WHERE userid = %s AND name = %s"

        try:
            self.cursor.execute(query, (new_name, userid, current_name))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error updating collection name:", e)
            self.cursor.connection.rollback()
            return False
        
    """
    Deletes movie from existing collection
    """
    def delete_movie_from_collection(self, coll_name, movname):
        movid = self.get_movid(movname)
        query = "DELETE FROM collectionofmovies WHERE name = %s AND movid = %s"
        
        try:
            self.cursor.execute(query, (coll_name, movid))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error deleting movie from collection:",  e)
            self.cursor.connection.rollback()
            return False

    def delete_collection(self, userid, name):
        query = "DELETE FROM collection WHERE userid = %s AND name ILIKE %s"

        try:
            self.cursor.execute(query, (userid, name))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error updating collection name:", e)
            self.cursor.connection.rollback()
            return False

    def follow_user(self, userid, friendid):
        query = "INSERT INTO friend (userid1, userid2) VALUES (%s, %s)" 

        try:
            self.cursor.execute(query, (userid, friendid,))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error failed to follow user:", e)
            return False

    def unfollow_user(self, userid, friendid):
        query = "DELETE FROM friend WHERE userid1 IN (%s, %s) AND userid2 IN (%s, %s)"

        try:
            self.cursor.execute(query, (userid, friendid, userid, friendid,))
            self.cursor.connection.commit()
            return True
        except Exception as e:
            print("Error failed to unfollow user:", e)
            return False
        
    def search_by_name(self, name):
        query = """
            SELECT m.title, m.length, m.agerating, r.userrating, 
                STRING_AGG(DISTINCT a.name, ', ') AS cast_members, 
                STRING_AGG(DISTINCT c.name, ', ') AS directors,
                STRING_AGG(DISTINCT g.genreType, ', ') AS genres
            FROM movies m
            LEFT JOIN rating r ON m.movID = r.movID
            LEFT JOIN acts_in ai ON m.movID = ai.movID
            LEFT JOIN contributors a ON ai.ID = a.ID
            LEFT JOIN directs d ON m.movID = d.movID
            LEFT JOIN contributors c ON d.ID = c.ID
            LEFT JOIN moviesHasGenre mg ON m.movID = mg.movID
            LEFT JOIN genre g ON mg.genreID = g.genreID
            WHERE LOWER(m.title) LIKE %s
            GROUP BY m.title, m.length, m.agerating, r.userrating
            ORDER BY m.title
        """
        search = '%' + name.lower() + '%'
        self.cursor.execute(query, (search,))
        results = self.cursor.fetchall()

        if not results:
            return None
        else:
            return results
        
    def search_by_release_date(self, release_date):
        query = """
            SELECT m.title, m.length, m.agerating, r.userrating, 
                STRING_AGG(DISTINCT a.name, ', ') AS cast_members, 
                STRING_AGG(DISTINCT c.name, ', ') AS directors,
                STRING_AGG(DISTINCT g.genreType, ', ') AS genres
            FROM movies m
            JOIN releasing rel ON m.movID = rel.movID
            LEFT JOIN rating r ON m.movID = r.movID
            LEFT JOIN acts_in ai ON m.movID = ai.movID
            LEFT JOIN contributors a ON ai.ID = a.ID
            LEFT JOIN directs d ON m.movID = d.movID
            LEFT JOIN contributors c ON d.ID = c.ID
            LEFT JOIN moviesHasGenre mg ON m.movID = mg.movID
            LEFT JOIN genre g ON mg.genreID = g.genreID
            WHERE rel.releasedate = %s
            GROUP BY m.title, m.length, m.agerating, r.userrating
            ORDER BY m.title
        """
        self.cursor.execute(query, (release_date,))
        results = self.cursor.fetchall()

        if not results:
            return None
        else:
            return results

    def search_by_cast(self, cast_member):
        query = """
            SELECT m.title, m.length, m.agerating, r.userrating, 
                STRING_AGG(DISTINCT a.name, ', ') AS cast_members, 
                STRING_AGG(DISTINCT c.name, ', ') AS directors,
                STRING_AGG(DISTINCT g.genreType, ', ') AS genres
            FROM movies m
            LEFT JOIN rating r ON m.movID = r.movID
            LEFT JOIN acts_in ai ON m.movID = ai.movID
            LEFT JOIN contributors a ON ai.ID = a.ID
            LEFT JOIN directs d ON m.movID = d.movID
            LEFT JOIN contributors c ON d.ID = c.ID
            LEFT JOIN moviesHasGenre mg ON m.movID = mg.movID
            LEFT JOIN genre g ON mg.genreID = g.genreID
            WHERE LOWER(a.name) LIKE %s
            GROUP BY m.title, m.length, m.agerating, r.userrating
            ORDER BY m.title
        """
        search = '%' + cast_member.lower() + '%'
        self.cursor.execute(query, (search,))
        results = self.cursor.fetchall()

        if not results:
            return None
        else:
            return results

    def search_by_studio(self, studio_name):
        query = """
            SELECT m.title, m.length, m.agerating, r.userrating, 
                STRING_AGG(DISTINCT a.name, ', ') AS cast_members, 
                STRING_AGG(DISTINCT c.name, ', ') AS directors,
                STRING_AGG(DISTINCT g.genreType, ', ') AS genres
            FROM movies m
            LEFT JOIN rating r ON m.movID = r.movID
            LEFT JOIN acts_in ai ON m.movID = ai.movID
            LEFT JOIN contributors a ON ai.ID = a.ID
            LEFT JOIN directs d ON m.movID = d.movID
            LEFT JOIN contributors c ON d.ID = c.ID
            LEFT JOIN produces p ON m.movID = p.movID
            LEFT JOIN contributors s ON p.ID = s.ID
            LEFT JOIN moviesHasGenre mg ON m.movID = mg.movID
            LEFT JOIN genre g ON mg.genreID = g.genreID
            WHERE LOWER(s.name) LIKE %s
            GROUP BY m.title, m.length, m.agerating, r.userrating
            ORDER BY m.title
        """
        search = '%' + studio_name.lower() + '%'
        self.cursor.execute(query, (search,))
        results = self.cursor.fetchall()

        if not results:
            return None
        else:
            return results

    def search_by_genre(self, genre_name):
        query = """
            SELECT m.title, m.length, m.agerating, r.userrating, 
                STRING_AGG(DISTINCT a.name, ', ') AS cast_members, 
                STRING_AGG(DISTINCT c.name, ', ') AS directors,
                g.genreType AS genre
            FROM movies m
            LEFT JOIN rating r ON m.movID = r.movID
            LEFT JOIN acts_in ai ON m.movID = ai.movID
            LEFT JOIN contributors a ON ai.ID = a.ID
            LEFT JOIN directs d ON m.movID = d.movID
            LEFT JOIN contributors c ON d.ID = c.ID
            LEFT JOIN moviesHasGenre mhg ON m.movID = mhg.movID
            LEFT JOIN genre g ON mhg.genreID = g.genreID
            WHERE LOWER(g.genretype) LIKE %s
            GROUP BY m.title, m.length, m.agerating, r.userrating, g.genreType
            ORDER BY m.title
        """
        search = '%' + genre_name.lower() + '%'
        self.cursor.execute(query, (search,))
        results = self.cursor.fetchall()

        if not results:
            return None
        else:
            return results
