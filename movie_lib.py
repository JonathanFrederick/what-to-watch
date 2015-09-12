"""Movie Library"""

class User:

    def __init__(self, user_id, **kwargs):
        self.ident = user_id
#        self.age = user_age
#        self.gender = user_gender
#        self.occupation = user_occupation
        self.user_ratings = {}

    def get_ratings(self, rating_list):
        self.user_ratings = {rat[1] : Rating(rat[2]) for rat in rating_list if rat[0] == self.ident}
        return self.user_ratings

class Rating:

    def __init__(self, rating, rating_user=None, rating_item=None, **kwargs):
        self.user_id = rating_user
        self.item_id = rating_item
        self.stars = rating
#        self.timestamp = rating_timestamp

    def __repr__(self):
        return 'Rating({})'.format(self.stars)


class Movie:

    def __init__(self, movie_id, movie_title, **kwargs):
        self.ident = movie_id
        self.title = movie_title
#        self.release = release_date
#        self.vid_release = video_release_date
#        self.url = imdb_url
#        self.genres = [*args]
#        self.genre_names = ['unknown', 'Action', 'Adventure', 'Animation',
#                            'Children\'s', 'Comedy', 'Crime', 'Documentary',
#                            'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical',
#                            'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
        self.movie_ratings = []
        self.avg_ratings = None

    def get_ratings(self, rating_list):
        self.movie_ratings = {rat[0] : Rating(rat[2]) for rat in rating_list if rat[1] == self.ident}
        return self.movie_ratings

    def avg_ratings(self, rating_list):
        self.avg_ratings = sum(get_ratings(rating_list))/len(self.movie_ratings)

    def name_for_id(self, ident):
        if self.ident == ident:
            return self.title



def main():
    pass



if __name__ == '__main__':
    main()
