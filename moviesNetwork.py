import networkx as nx
import pandas as pd

G = nx.Graph()

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

actorsMovies = {}

for k in range(len(sheet['Actors'])):
    actors = sheet['Actors'][k].split(",")
    movie = sheet['Title'][k].strip()

    G.add_node(movie)

    for i in range(len(actors)):
        actors[i] = actors[i].strip()

    for actor in actors:
        if (not actor in actorsMovies):
            actorsMovies[actor] = []

        actorsMovies[actor].append(movie)


for value in actorsMovies.values():
    if (len(value) > 1):
        for i in range(len(value) - 1):
            for j in range(i + 1, len(value)):
                if (not G.has_edge(value[i], value[j])):
                    G.add_edge(value[i], value[j])

nx.write_gml(G, "files/moviesNetwork.gml")

