import pandas as pd

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

genresToMovies = {}

for genreList in sheet['Genre']:
    genres = genreList.split(",")

    for i in range(len(genres)):
        genres[i] = genres[i].strip()

        if not genres[i] in genresToMovies:
            genresToMovies[genres[i]] = 1
        else:
            genresToMovies[genres[i]] += 1

genresToMovies = {k: v for k, v in sorted(genresToMovies.items(), key=lambda x: x[1], reverse=True)}

file = open("files/mostPopularGenres.txt", "w+")

for key, value in genresToMovies.items():
    file.write("Genre: %s , Number of movies: %d.\n" % (key, value))

file.close()
