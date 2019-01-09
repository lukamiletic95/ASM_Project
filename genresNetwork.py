import networkx as nx
import pandas as pd

G = nx.Graph()

sheet = pd.read_csv(r"files/IMDB-Movie-Data.csv")

for genreList in sheet['Genre']:
    genres = genreList.split(",")

    for i in range(len(genres)):
        genres[i] = genres[i].strip()

    for i in range(len(genres) - 1):
        for j in range(i + 1, len(genres)):
            if (G.has_edge(genres[i], genres[j])):
                G[genres[i]][genres[j]]['weight'] = G[genres[i]][genres[j]]['weight'] + 1
            else:
                G.add_edge(genres[i], genres[j])
                G[genres[i]][genres[j]]['weight'] = 1

nx.write_gml(G, "files/genresNetwork.gml")
