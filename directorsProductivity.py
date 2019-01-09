import pandas as pd

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

productivity = {}

for director in sheet['Director']:
    director = director.strip()

    if (director in productivity):
        productivity[director] = productivity[director] + 1
    else:
        productivity[director] = 1

productivity = {k: v for k, v in sorted(productivity.items(), key=lambda x: x[1], reverse=True)}

sumProductivity = 0
for value in productivity.values():
    sumProductivity += value

file = open("files/directorsProductivity.txt", "w+")

file.write("Average productivity: " + str(sumProductivity / len(productivity)) + "\n\n")

for key, value in productivity.items():
    file.write(key + ": " + str(value) + "\n")

file.close()
