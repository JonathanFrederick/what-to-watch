from movie_lib import *

users = {123:User(234), 345:User(456), 567:User(678)}
movies = {543:Movie(876, "A Bug's Life"), 321:Movie(987, 'Toy Story'), 432:Movie(654, 'The Incredibles')}
           #usr, mov, rating
ratings = [[234, 987, 3],
           [234, 876, 4],
           [678, 987, 5],
           [456, 876, 4],
           [678, 654, 3],
           [456, 321, 2]]

def test_user_init():
    """tests User init"""
    assert users[123].ident == 234
    assert users[123].ident != 123
    assert users[345].ident == 456
    assert users[567].ident == 678

def test_user_get_ratings():
    """tests User.get_ratings() and Rating.__init__"""
    for user in users:
         users[user].get_ratings(ratings)
    users[123].user_ratings[987].stars == 3
    users[123].user_ratings[987].stars != 2
    users[345].user_ratings[876].stars == 4
    users[567].user_ratings[987].stars == 5


    # assert users[123].user_ratings == {987: Rating(3), 876: Rating(4)}
    # assert users[345].user_ratings == {876: Rating(4), 321: Rating(2)}
    # assert users[567].user_ratings == {987: Rating(5), 654: Rating(3)}

def test_movie_init():
    """tests Movie init"""
    assert movies[543].ident == 876
    assert movies[543].title == "A Bug's Life"
    assert movies[321].ident == 987
    assert movies[321].title == "Toy Story"
    assert movies[432].ident == 654
    assert movies[432].title == "The Incredibles"
    assert movies[432].ident != 135
    assert movies[432].title != "Cars"

def test_movie_get_ratings():
    """tests Movie.get_ratings"""
    for movie in movies:
        movies[movie].get_ratings(ratings)
    assert movies[543].movie_ratings[456].stars == 4
    assert movies[543].movie_ratings[234].stars == 4
    assert movies[543].movie_ratings[234].stars != 2
    assert movies[321].movie_ratings[234].stars == 3
    assert movies[321].movie_ratings[678].stars == 5
    assert movies[432].movie_ratings[678].stars == 3



# def test_movie_avg_ratings():
#     """tests avg_ratings"""
