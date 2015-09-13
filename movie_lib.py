"""Movie Library"""
import csv


all_movies = {}
all_users = {}


class User:

    def __init__(self, user_id, **kwargs):
        self.ident = user_id
#        self.age = user_age
#        self.gender = user_gender
#        self.occupation = user_occupation
        self.ratings = {}
        all_users[self.ident] = self

    def add_rating(self,rating):
        self.ratings[rating.item_id] = rating

    def get_ratings(self):
        return self.ratings.values()

    def __str__(self):
        return 'User(user_id={})'.format(self.ident)

    def __repr__(self):
        return self.__str__()

class Rating:

    def __init__(self, rating_user, rating_item, rating, **kwargs):
        self.user_id = rating_user
        self.item_id = rating_item
        self.stars = rating
#        self.timestamp = rating_timestamp

        all_movies[self.item_id].add_rating(self)
        all_users[self.user_id].add_rating(self)


    def __str__(self):
        return 'Rating(rating_user={}, rating_item={}, rating={})'.format(self.user_id, self.item_id, self.stars)

    def __repr__(self):
        return self.__str__()


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
        self.ratings = {}
        all_movies[self.ident] = self


    def add_rating(self, rating):
        self.ratings[rating.user_id] = rating

    def get_ratings(self):
        return self.ratings.values()

    def avg_ratings(self):
        return sum([x.stars for x in self.get_ratings()])/len(self.ratings)

    def name_for_id(self, ident):
        if self.ident == ident:
            return self.title

    def __str__(self):
        return 'Movie(movie_id={}, movie_title={})'.format(self.ident, repr(self.title))

    def __repr__(self):
        return self.__str__()


def load_movies():
    with open('ml-100k/u.item', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title', '', '', 'something_else' ], delimiter='|')
        for row in reader:
            Movie(int(row['movie_id']), row['movie_title'])

def load_users():
    with open('ml-100k/u.user') as f:
        reader = csv.DictReader(f, fieldnames=['user_id'], delimiter='|')
        for row in reader:
            User(int(row['user_id']))

def load_ratings():
    with open('ml-100k/u.data') as f:
        reader = csv.DictReader(f, fieldnames=['user_id', 'item_id', 'rating'], delimiter='\t')
        for row in reader:
            Rating(int(row['user_id']), int(row['item_id']), int(row['rating']))

def load_data():
    load_movies()
    load_users()
    load_ratings()



def main():
    load_data()
    print(all_movies[1].ratings)



if __name__ == '__main__':
    main()
