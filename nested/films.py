movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]
# q1 total_number_of_movies

movies_count=len(movies)
# print("movie_count",movies_count)

#q2 movies with genre Drama

drama_movies=[m.get("title")for m in movies if "Drama" in m.get("genres")]
# print(drama_movies)

#q3 latest movie
def get_year(m):
    return m.get("year")
latest_movie=max(movies,key=get_year) 
latest_movies=[m.get("title") for m in movies if m.get("year")==latest_movie.get("year")]
# print(latest_movies)

#q4 top movie (movie with higest rating)


def get_rating(m):
    return m.get("rating")
highest_rating=max(movies,key=get_rating)
highest_rating_mov=[m.get("title") for m in movies if m.get("rating")==highest_rating.get("rating")]
# print(highest_rating_mov)


#q5 movies with language malayalam
mal_movie=[m.get("title")for m in movies if m.get("language")=="Malayalam"]
# print(mal_movie)


# q6 movies released after year 2016

mov=[m.get("title") for m in movies if m.get("year")>2016]
# print(mov)

#q7 movie with lowest rating

def get_rating(m):
    return m.get("rating")
lowest_rating=min(movies,key=get_rating) 
lowest_rating_mov=[m.get("title")for m in movies if m.get("rating")==lowest_rating.get("rating")]   
# print(lowest_rating_mov)

#q8 malayalam movies with genere Action

genre_filter=[m.get("title")for m in movies if "Malayalam" in m.get("language") and "Action" in m.get("genres")]
# print(genre_filter)


#q9 movies releasd in same years






# q10 oldest movie
def get_year(m):
    return m.get("year")
oldest_movie=min(movies,key=get_year) 
oldest_movies=[m.get("title") for m in movies if m.get("year")==oldest_movie.get("year")]
# print(oldest_movies)


# movie name with generes either Drama or Comedy
genre_filter=[m.get("title")for m in movies if ("Drama" or "Comedy") in m.get("genres")]
# print(genre_filter)
