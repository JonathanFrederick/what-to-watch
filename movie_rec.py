"""This is a program to recommend movies based on user preference"""
from movie_lib import *
import sys

def get_int(low, high, prompt):
    """Prompts the player for an integer within a range"""
    while True:
        try:
            integer = int(input(prompt))
            if integer < low or integer > high:
                integer/0
            break
        except:
            print("Please enter an integer between", low, "and", high)
            continue
    return integer

def rate_movie():
    while True:
        try:
            iden = int(input("Please enter the ID of the movie you'd like to rate >>"))
        except:
            print("Not a valid movie ID")
        if iden in all_movies:
            rate = get_int(0, 5, "Please enter your selected rating for "+all_movies[iden].title+"\nEnter a number 1 through 5 where 5 is more favorable or enter 0 to back out >>")
            if rate > 0:
                Rating(0, iden, rate)
            break
        else:
            print("Not a valid movie ID")

def search_movies():
    string = input("Please enter all or part of a movie title >> ").title()
    print("ID\tTITLE")
    for movie in all_movies.values():
        if string in movie.title:
            print(str(movie.ident)+'\t'+movie.title)

def main_menu():
    while True:
        choice = get_int(1, 5, """Please select an option:
    1 - View movies by highest average rating
    2 - Search for a movie
    3 - Rate a movie by ID
    4 - Get recommendations (must have rated at least 4 movies)
    5 - Exit
>>>""")
        if choice == 1:
            print_movies_by_avg()
        elif choice == 2:
            search_movies()
        elif choice == 3:
            rate_movie()
        elif choice == 4:
            if len(all_users[0].ratings) > 3:
                num = get_int(1, 20, "Please enter a desired number of recommendations between 1 and 20")
                for movie in all_users[0].recommendations(num):
                    print(movie.title)

            else:
                print("Rate more movies for this feature")
        else:
            sys.exit()

def main():
    load_data()
    all_users[0] = User(0)
    main_menu()


if __name__ == '__main__':
    main()
