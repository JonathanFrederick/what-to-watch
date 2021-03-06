"""Movie Library"""
import csv
import math


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

    def get_similar_users(self):
        return sorted([user for user in all_users.values() if euclidean_distance(*euclid_prep(self, user)) < .33], key=lambda u: euclidean_distance(*euclid_prep(self, u)), reverse=True)

    def recommendations(self, num):
        recs = {}
        while len(recs) < num*5:
            for usr in self.get_similar_users():
                for rat in usr.ratings.values():
                    if rat.item_id not in self.ratings and rat.stars > 3:
                        if rat.item_id in recs:
                            holder = rat.stars*euclidean_distance(*euclid_prep(self, usr))
                            if holder > recs[rat.item_id][1]:
                                recs[rat.item_id] = [rat, holder]
                        else:
                            recs[rat.item_id] = [rat, rat.stars*euclidean_distance(*euclid_prep(self, usr))]
        sort_recs = sorted(recs.values(), key=lambda r: r[1], reverse=True)
        return [all_movies[x[0].item_id] for x in sort_recs][:num]


    def get_top(self, num):
       return sorted([mov for mov in all_movies.values()
                          if mov.ident not in self.ratings],
                     key=lambda m: m.avg_ratings(), reverse=True)[:num]


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
        return round(sum([x.stars for x in self.get_ratings()])/len(self.ratings),1)

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

def euclidean_distance(list_1, list_2): #takes in two User objects
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """
    # Guard against empty lists.
    if len(list_1) is 0:
        return 0
    # Note that this is the same as vector subtraction.
    differences = [list_1[idx] - list_2[idx] for idx in range(len(list_1))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)
    return 1 / (1 + math.sqrt(sum_of_squares))


def euclid_prep(user_1, user_2):
    list_1=[y.stars for y in sorted([x for x in user_1.ratings.values() if x.item_id in user_2.ratings], key=lambda r:r.item_id)]
    list_2=[y.stars for y in sorted([x for x in user_2.ratings.values() if x.item_id in user_1.ratings], key=lambda r:r.item_id)]
    return list_1, list_2

def print_movies_by_avg():
    count = 1
    for movie in sorted(all_movies.values(), key=lambda m: m.avg_ratings(), reverse=True):
        if count % 20 == 1:
            print("RANK\tID\tAVG\tTITLE")
        print(count, '\t'+str(movie.ident), '\t'+str(movie.avg_ratings()), '\t'+movie.title)
        if count % 20 == 0:
            input("Press enter to view the next 20")
        count+=1


def main():
    load_data()
    #print(euclidean_distance(*euclid_prep(all_users[1], all_users[2])))
    #print([euclidean_distance(*euclid_prep(all_users[1], user)) for user in all_users[1].get_similar_users()])
    print(all_users[1].recommendations(10))


if __name__ == '__main__':
    main()
