import pandas as pd

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

movieProduction= {}

for year in sheet['Year']:
    if (not year in movieProduction):
        movieProduction[year] = 1
    else:
        movieProduction[year] += 1

movieProduction = {k: v for k, v in sorted(movieProduction.items(), key=lambda x: x[1], reverse=True)}

file = open("files/movieProduction.txt", "w+")

for key, value in movieProduction.items():
    file.write("Year: %d , Number of movies: %d.\n" % (key, value))

file.close()