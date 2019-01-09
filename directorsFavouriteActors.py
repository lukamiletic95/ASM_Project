import pandas as pd

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

directorsDictionary = {}

for k in range(len(sheet['Actors'])):
    actors = sheet['Actors'][k].split(",")
    director = sheet['Director'][k].strip()

    for i in range(len(actors)):
        actors[i] = actors[i].strip()

    if (not director in directorsDictionary):
        directorsDictionary[director] = {}

    for i in range(len(actors)):
        if (actors[i] in directorsDictionary[director]):
            directorsDictionary[director][actors[i]] = directorsDictionary[director][actors[i]] + 1
        else:
            directorsDictionary[director][actors[i]] = 1

for d in directorsDictionary.keys():
    directorsDictionary[d] = {k: v for k, v in sorted(directorsDictionary[d].items(), key=lambda x: x[1], reverse=True)}

file = open("files/directorsFavouriteActors.txt", "w+")

for key, value in directorsDictionary.items():
    file.write("*** " + key + " ***\n")

    for key1, value1 in value.items():
        file.write(key1 + ": " + str(value1) + "\n")

    file.write('\n')

file.close()
