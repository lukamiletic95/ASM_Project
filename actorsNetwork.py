import networkx as nx
import pandas as pd

G = nx.Graph()

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

for actorList in sheet['Actors']:
    actors = actorList.split(",")

    for i in range(len(actors)):
        actors[i] = actors[i].strip()

    for i in range(len(actors) - 1):
        for j in range(i + 1, len(actors)):
            if (G.has_edge(actors[i], actors[j])):
                G[actors[i]][actors[j]]['weight'] = G[actors[i]][actors[j]]['weight'] + 1
            else:
                G.add_edge(actors[i], actors[j])
                G[actors[i]][actors[j]]['weight'] = 1


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

for actor, genres in actorsDictionary.items():
    topThreeGenres = ""

    i = 0

    for genreName in genres.keys():
        topThreeGenres += genreName

        if (i < 2):
            topThreeGenres += ", "

        i += 1

        if (i == 3):
            break

    attributes = {actor: {'topThreeGenres': topThreeGenres}}
    nx.set_node_attributes(G, attributes)

nx.write_gml(G, "files/actorsNetwork.gml")
