import pandas as pd

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

actorsDictionary = {}

for k in range(len(sheet['Actors'])):
    actors = sheet['Actors'][k].split(",")
    genres = sheet['Genre'][k].split(",")

    for i in range(len(actors)):
        actors[i] = actors[i].strip()

    for i in range(len(genres)):
        genres[i] = genres[i].strip()

    for i in range(len(actors)):

        if (not actors[i] in actorsDictionary):
            actorsDictionary[actors[i]] = {}

        for j in range(len(genres)):

            if (genres[j] in actorsDictionary[actors[i]]):
                actorsDictionary[actors[i]][genres[j]] = actorsDictionary[actors[i]][genres[j]] + 1
            else:
                actorsDictionary[actors[i]][genres[j]] = 1

for actor in actorsDictionary.keys():
    actorsDictionary[actor] = {k: v for k, v in
                               sorted(actorsDictionary[actor].items(), key=lambda x: x[1], reverse=True)}

file = open("files/actorsGenres.txt", "w+")

for key, value in actorsDictionary.items():
    file.write("*** " + key + " ***\n")

    for key1, value1 in value.items():
        file.write(key1 + ": " + str(value1) + "\n")

    file.write('\n')

file.close()
