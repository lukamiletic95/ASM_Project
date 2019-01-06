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

nx.write_gml(G, "files/actorsNetwork.gml")
