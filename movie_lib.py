"""Movie Library"""

class User:

    def __init__(self, ident, user_age, user_gender, user_occupation, zip_code):
        self.user_id = ident
        self.age = user_age
        self.gender = user_gender
        self.occupation = user_occupation


class Rating:

    def __init__(self, rating_user, rating_item, rating_, rating_timestamp):
        self.user_id = rating_user
        self.item_id = rating_item
        self.rating = rating_
        self.timestamp = rating_timestamp


class Movie:

    def __init__(self, movie_id, movie_title, release_date, video_release_date, imdb_url, *args):
        self.item_id = movie_id
        self.title = movie_title
        self.release = release_date
        self.vid_release = video_release_date
        self.url = imdb_url
        self.genres = [*args]
        self.genre_names = ['unknown', 'Action', 'Adventure', 'Animation',
                            'Children\'s', 'Comedy', 'Crime', 'Documentary',
                            'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
                            'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']





def main():
    pass



if __name__ == '__main__':
    main()
