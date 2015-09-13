from movie_lib import *

load_data()
#   PRE LOADED DATA NUMBERS
# users = [User(234), User(456), User(678)]
# movies = [Movie(87, "A Bug's Life"), Movie(98, 'Toy Story'), Movie(65, 'The Incredibles')]
#                  #usr, mov, rating
# ratings = [Rating(234, 98, 3),
#            Rating(234, 87, 4),
#            Rating(678, 98, 5),
#            Rating(456, 87, 4),
#            Rating(678, 65, 3),
#            Rating(456, 65, 2)]

def test_user_init():
    """tests User init"""
    assert all_users[234].ident == 234
    assert all_users[234].ident != 123
    assert all_users[456].ident == 456
    assert all_users[678].ident == 678

def test_user_ratings():
    """tests User.add_rating and Rating.__init"""
    print(all_users[6].ratings)
    all_users[2].ratings[257].stars == 4
    all_users[4].ratings[258].stars == 5
    all_users[6].ratings[512].stars == 4
    all_users[6].ratings[512].stars != 5
    # all_users[234].ratings[98].stars == 3
    # all_users[234].ratings[98].stars != 2
    # all_users[456].ratings[87].stars == 4
    # all_users[678].ratings[98].stars == 5

def test_user_get_ratings():
    """tests User.get_ratings"""
    # PRE LOAD DATA FUNCTIONS
    # assert sum([x.stars for x in all_users[234].get_ratings()]) == 7
    # assert sum([x.stars for x in all_users[678].get_ratings()]) == 8
    # assert sum([x.stars for x in all_users[456].get_ratings()]) == 6
    assert sum([x.stars for x in all_users[3].get_ratings()]) == 151
    assert sum([x.stars for x in all_users[6].get_ratings()]) == 767
    assert sum([x.stars for x in all_users[9].get_ratings()]) == 94


def test_user_get_top_list():
    """tests User.get_top"""
    assert 814 not in all_users[1].ratings
    assert len(all_users[1].get_top(10)) == 10
    assert all_users[1].get_top(10)[0].avg_ratings() > all_users[1].get_top(20)[19].avg_ratings()


def test_movie_init():
    """tests Movie init"""
    assert all_movies[87].ident == 87
    assert all_movies[98].ident == 98
    assert all_movies[65].ident == 65
    assert all_movies[65].ident != 13
    assert all_movies[87].title == "Searching for Bobby Fischer (1993)"
    assert all_movies[98].title == "Silence of the Lambs, The (1991)"
    assert all_movies[65].title == "What's Eating Gilbert Grape (1993)"
    assert all_movies[65].title != ""
    #PRE LOAD DATA
    # assert all_movies[98].title == "Toy Story"
    # assert all_movies[65].title == "The Incredibles"
    # assert all_movies[87].title == "A Bug's Life"
    # assert all_movies[65].title != "Cars"

def test_movie_ratings():
    """tests Movie.add_ratings"""
    assert all_movies[10].ratings[514].stars == 4
    assert all_movies[10].ratings[514].stars != 3
    assert all_movies[12].ratings[250].stars == 5

    #PRE LOAD DATA
    # assert all_movies[98].ratings[234].stars == 3
    # assert all_movies[87].ratings[234].stars == 4
    # assert all_movies[87].ratings[234].stars != 2
    # assert all_movies[98].ratings[678].stars == 5
    # assert all_movies[87].ratings[456].stars == 4
    # assert all_movies[65].ratings[678].stars == 3

def test_movie_avg_ratings():
    """tests Movie.get_ratings and Movie.avg_ratings"""
    print(all_movies[22].avg_ratings())
    assert all_movies[20].avg_ratings() == 3.4
    assert all_movies[21].avg_ratings() == 2.8
    assert all_movies[22].avg_ratings() == 4.2
    #PRE LOAD DATA
    # assert all_movies[98].avg_ratings() == 4.0
    # assert all_movies[87].avg_ratings() == 4.0
    # assert all_movies[65].avg_ratings() == 2.5


def test_load_data():

    pass

# def test_movie_avg_ratings():
#     """tests avg_ratings"""
