from movie_lib import *

users = {123:User(234), 345:User(456), 567:User(678)}
ratings = [[234, 987, 3],
           [234, 876, 4],
           [678, 987, 5],
           [456, 876, 4],
           [678, 654, 3],
           [456, 321, 2]]

def test_user_init():
    assert users[123].user_id == 234
    assert users[123].user_id != 123
    assert users[345].user_id == 456
    assert users[567].user_id == 678

def test_user_get_ratings():
    for user in users:
        print(type(users[user]))
        print(users[user].get_ratings(ratings))
    assert users[123].user_ratings == {987 : 3, 876 : 4}
    assert users[345].user_ratings == {876 : 4, 321 : 2}
    assert users[567].user_ratings == {987 : 5, 543 : 3}
