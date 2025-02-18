from datetime import datetime
from Entities.User import User
import os
import time
from hashlib import sha256

class CLI_Handler:
    def __init__(self, cursor):
        self.cursor = cursor
        self.User = User(cursor)

    def Security_Screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')        

        choice = input("Login or Create Account: ")
        choice = choice.lower()

        if(choice == "create account"):
            self.Create_Account()
            return "valid"
        elif(choice == "login"):
            valid = self.Login()
            while(not valid):
                print("Invalid username or password, please try again.")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                valid = self.Login()

            os.system('cls' if os.name == 'nt' else 'clear')
            self.User.update_lastaccess(datetime.now())
            return "valid" 
        else:
            print("Invalid choice.")
            time.sleep(1)
            self.Security_Screen()

    def Login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Verify credentials
        shapassword = sha256(password.encode('utf-8')).hexdigest()
        valid = self.User.check_credentials(username, shapassword)

        if valid is not None:
            self.User.update_all_info(valid['userid'], valid['lastaccess'], valid['creationdate'], valid['username'], 
                                      valid['password'], valid['email'], valid['firstname'], valid['lastname'])
            return True
        else:
            return False
        
    def Create_Account(self):
        firstname = input("First name: ")
        lastname = input("Last name: ")
        email = input("Email: ")
        username = input("Create username: ")

        # Validate to see if username is taken
        taken = self.User.check_credentials(username, None)

        if(taken):
            print("Username taken, please try a different one.")
            self.Create_Account()
        
        password = input("Create password: ")
        conf_password = input("Confirm password: ")

        while(password != conf_password):
            print("Passwords do not match, please try again")
            password = input("Create password: ")
            conf_password = input("Confirm password: ")
        shapassword = sha256(password.encode('utf-8')).hexdigest()

        self.User.add_account(firstname, lastname, email, username, shapassword, datetime.now())

        print("Login with your new account credentials.")
        self.Security_Screen()

    def Main_Menu(self):
        print("Welcome " + self.User.get_username() + "!")
        while True:
            print("")
            print("1. Collections")
            print("2. Search Movie")
            print("3. Movie Recommendations")
            print("4. Search User")
            print("5. View Profile")
            print("6. Quit")
            
            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                while True:
                    print("\nShow All")
                    print("Create (insert name)")
                    print("Select (insert name)")
                    print("Delete (insert name)")
                    print("Back\n")

                    choice = input("Enter your choice: ")
                    choice = choice.lower()

                    if(choice == "show all"):
                        self.User.list_collections()
                        continue
                    elif(choice.startswith("create ")):
                        name = choice.split(" ", 1)[1].strip()
                        self.User.create_collection(name)
                    elif(choice.startswith("select ")):
                        name = choice.split(" ", 1)[1].strip()
                        while True:
                            print("\nPlay All")
                            print("List Movies")
                            print("Change Name")
                            print("Add (insert movie name)")
                            print("Select (insert movie name)")
                            print("Back\n")

                            choice = input("Enter your choice: ")
                            choice = choice.lower()

                            if(choice == "play all"):
                                self.User.play_collection(name)
                            elif(choice == "list movies"):
                                self.User.list_movies_in_collection(name)
                            elif(choice == "change name"):
                                new_name = input("Enter new collection name: ")
                                self.User.change_collection_name(name, new_name)
                                name = new_name
                                print("Successfully changed collection name to " + name + "!")
                            elif(choice.startswith("add ")):
                                title = choice.split(" ", 1)[1].strip()
                                self.User.add_to_collection(name, title)
                                print("Movie added!")
                            elif(choice.startswith("select ")):
                                title = choice.split(" ", 1)[1].strip()
                                print("\nPlay")
                                print("Rate")
                                print("Remove\n")
                                print("Back\n")
                                
                                choice = input("Enter your choice: ")
                                choice = choice.lower()

                                if(choice == "play"):
                                    print("Playing " + title + "...")
                                    self.User.play_movie(title)
                                    print("Finished playing " + title + "!\n")
                                    
                                elif(choice == "rate"):
                                    rating = input("What would you like to rate this movie (1-5): ")
                                    self.User.rate_movie(title, rating)
                                    print("Your rated the movie a " + str(rating) + " out of 5!")
                                elif(choice == "remove"):
                                    self.User.delete_from_collection(name, title)
                                    print("Movie removed!")
                                    break # No reason to stay in loop if deleted
                                elif(choice == "back"):
                                    break
                                else:
                                    print("Invalid choice, please choose an option above.")
                            elif(choice == "back"):
                                break
                            else:
                                print("Invalid choice, please choose an option above.")

                    elif(choice.startswith("delete ")):
                        name = choice.split(" ", 1)[1].strip()
                        self.User.delete_collection(name)
                        print("Successfully deleted collection!")
                    elif(choice == "back"):
                        break
                    else:
                        print("Invalid choice, please choose an option above.")

            elif choice == "2":
                # Call function to search for movies
                while True:
                    print("\n1. Search by Name")
                    print("2. Search by Release Date")
                    print("3. Search by Cast")
                    print("4. Search by Studio")
                    print("5. Search by Genre")
                    print("6. Quit")

                    choice = input("\nEnter your choice (1-6): ")

                    if(int(choice) < 1 or int(choice) > 6):
                        print("Invalid choice, please choose an option above.")
                        continue
                    elif(choice == "6"):
                        break

                    search = input("Search: ").lower()
                    list_of_movies = self.User.search_movie(choice, search)

                    if(list_of_movies is not None):
                        wantSort = input("Would you like to sort this list? (y/n): ")

                        while True:
                            if(wantSort == "y"):
                                print("\n1. Sort by Name")
                                print("2. Sort by Release Date")
                                print("3. Sort by Studio")
                                print("4. Sort by Genre")
                                print("5. Quit")

                                sort_choice = input("\nEnter your choice (1-5): ")
                                if(sort_choice == "5"):
                                    break
                                else:
                                    up_or_down = input("Ascending or Descending? (A/D): ")
                                    if(int(sort_choice) > 0 and int(sort_choice) < 5):
                                        self.User.sort_movies(list_of_movies, sort_choice, up_or_down.lower())
                                    else:
                                        print("Invalid choice, please choose an option above.")
                                        continue
                            elif(wantSort == "n"):
                                break
                            else:
                                print("Invalid choice, please choose an option above.")
                                continue

                        wantSelect = input("\nWould you like to select a movie? (y/n): ")

                        if(wantSelect == "y"):
                            movie_name = input("Enter movie name: ")

                            cond = True
                            while cond:
                                print("\n Movie " + movie_name + " selected:")
                                print("1. Play")
                                print("2. Rate")
                                print("3. Add to Collection")
                                print("4. Back")

                                choice = input("\nEnter your choice (1-4): ")

                                while True:
                                    if(choice == "1"):
                                        print("Playing...")
                                        self.User.play_movie(movie_name)
                                        print("Finished playing.")
                                        break
                                    elif(choice == "2"):
                                        rating = input("What would you like to rate this movie (1-5): ")
                                        self.User.rate_movie(movie_name, rating)
                                        print("Your rated the movie a " + str(rating) + " out of 5!")
                                        break
                                    elif(choice == "3"):
                                        coll_name = input("Which collection would you like to add " + movie_name + " to: ")
                                        self.User.add_to_collection(coll_name, movie_name)
                                        print(movie_name + " successfully added to " + coll_name + "!")
                                        break
                                    elif(choice == "4"):
                                        cond = False
                                        break
                        elif(wantSelect == "n"):
                            break
                        else:
                            print("Invalid choice, please choose an option above.")
                            continue
            elif choice == "3":
                # Call function to handle Recommended Movies
                print("\nTop 20 Movies In The Last 90 Days: ")
                self.User.get_top_twenty_in_last_ninety_days()
                print("\nTop 20 Movies Among Your Followers: ")
                self.User.get_top_twenty_movies_among_followers()
                print("\nTop 5 New Releases This Month: ")
                self.User.get_top_five_new_releases()
                # recommendations
                self.User.get_recommendations()
            elif choice == "4":
                # Call function to handle Search User
                while True:
                    print("\nSearch User (by email)")
                    print("Quit")

                    choice = input("Enter your choice: ")
                    choice = choice.lower()

                    if(choice.startswith("search user ")):
                        user_email = choice.split(" ", 2)[2].strip()
                        user_id = self.User.check_user(user_email)
                        if (user_id != None): # user exists
                             user_id = user_id[0]
                             while True:
                                print("\nFollow")
                                print("Unfollow")
                                print("Quit")

                                choice = input("Enter your choice: ")
                                choice = choice.lower()

                                if(choice == "follow"):
                                    process = self.User.follow_user(user_id)
                                    if(process == True):
                                        print("Successful in following them")
                                        continue
                                    else:
                                        print("Failed to follow them")
                                elif(choice == "unfollow"):
                                    process = self.User.unfollow_user(user_id)
                                    if(process == True):
                                        print("Successful in unfollowing them")
                                        continue
                                    else:
                                        print("Failed to unfollow them")
                                elif(choice == "quit"):
                                    break
                                else:
                                    print("Invalid choice, please choose an option above.")
                        else:
                            print("User with the email ", user_email, " not found.")
                    elif(choice.startswith("quit")):
                        break
                    else:
                        print("Invalid choice, please choose an option above.")
            elif choice == "5":
                # Call function to view profile
                print("\nUser Profile")
                print("Full Name: " + self.User.get_firstname() + " " + self.User.get_lastname())
                print("Username: " + self.User.get_username())
                print("Email: " + self.User.get_email())
                print("Number of Collections: ", self.User.get_num_collections())
                print("Followers: ", self.User.get_num_followers())
                print("Following: ", self.User.get_num_following())
                print("Would you like to sort your top ten movies by Rating, Most Viewed, or Both?")
                sort_top_ten = input().lower()
                print("Top 10 Movies: ")
                self.User.get_top_ten_movies(sort_top_ten)
            elif choice == "6":
                # Call function to quit
                break
            else:
                print("Invalid choice, please select one of the choices above.")
                continue
