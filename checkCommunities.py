import imp

import pandas as pd

sheet = pd.read_csv(r"files/Communities.csv")
communities = {}

importantComunnities = [12, 24, 25, 6, 32]

for k in range(len(sheet['Label'])):
    if importantComunnities.__contains__(sheet['modularity_class'][k]):
        continue

    if not sheet['modularity_class'][k] in communities:
        communities[sheet['modularity_class'][k]] = {}

    if not sheet['topgenre'][k] in communities[sheet['modularity_class'][k]]:
        communities[sheet['modularity_class'][k]][sheet['topgenre'][k]] = 1
    else:
        communities[sheet['modularity_class'][k]][sheet['topgenre'][k]] += 1

for comunity in communities.keys():
    communities[comunity] = {k: v for k, v in sorted(communities[comunity].items(), key=lambda x: x[1], reverse=True)}

file = open("files/communitiesByGenre.txt", "w+")

for key, value in communities.items():
    file.write("*** " + str(key) + " ***\n")

    for key1, value1 in value.items():
        file.write(key1 + ": " + str(value1) + "\n")

    file.write('\n')

file.close()
