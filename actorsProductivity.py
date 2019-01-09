import pandas as pd

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

productivity = {}

for actorList in sheet['Actors']:
    actors = actorList.split(",")

    for i in range(len(actors)):
        actors[i] = actors[i].strip()

        if (actors[i] in productivity):
            productivity[actors[i]] = productivity[actors[i]] + 1
        else:
            productivity[actors[i]] = 1

productivity_sorted = {k: v for k, v in sorted(productivity.items(), key=lambda x: x[1], reverse=True)}

sumProductivity = 0
for value in productivity_sorted.values():
    sumProductivity += value

file = open("files/actorsProductivity.txt", "w+")

file.write("Average productivity: " + str(sumProductivity / len(productivity_sorted)) + "\n\n")

for key, value in productivity_sorted.items():
    file.write(key + ": " + str(value) + "\n")

file.close()
