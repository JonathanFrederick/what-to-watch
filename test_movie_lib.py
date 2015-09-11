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
    assert users[123].user_id == 234
    assert users[123].user_id != 123
    assert users[345].user_id == 456
    assert users[567].user_id == 678

def test_user_get_ratings():
    """tests User.get_ratings() and Rating.__init__"""
    for user in users:
         users[user].get_ratings(ratings)
    users[123].user_ratings[987].rating == 3
    users[123].user_ratings[987].rating != 2
    users[345].user_ratings[876].rating == 4
    users[567].user_ratings[987].rating == 5


    # assert users[123].user_ratings == {987: Rating(3), 876: Rating(4)}
    # assert users[345].user_ratings == {876: Rating(4), 321: Rating(2)}
    # assert users[567].user_ratings == {987: Rating(5), 654: Rating(3)}

def test_movie_init():
    """tests Movie init"""
    assert movies[543].item_id == 876
    assert movies[543].title == "A Bug's Life"
    assert movies[321].item_id == 987
    assert movies[321].title == "Toy Story"
    assert movies[432].item_id == 654
    assert movies[432].title == "The Incredibles"
    assert movies[432].item_id != 135
    assert movies[432].title != "Cars"

def test_movie_get_ratings():
    """tests Movie.get_ratings"""
    for movie in movies:
        movies[movie].get_ratings(ratings)
    print(movies[543].movie_ratings[456])
    print(movies[321])
    print(movies[432])
    assert movies[543].movie_ratings[456].rating == 4
    assert movies[543].movie_ratings[234].rating == 4
    assert movies[543].movie_ratings[234].rating != 2
    assert movies[321].movie_ratings[234].rating == 3
    assert movies[321].movie_ratings[678].rating == 5
    assert movies[432].movie_ratings[678].rating == 3
