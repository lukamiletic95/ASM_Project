import networkx as nx

G = nx.read_gml("files/actorsNetwork.gml")

kevinBacon = None

for node in G.nodes:
    if node == "Kevin Bacon":
        kevinBacon = node
        break

maxDistance = 0
sumShortestDistances = 0
numShortestDistances = 0
file = open("files/sixDegreesOfKevinBacon.txt", "w+")

for node in G.nodes:
    try:
        if node == kevinBacon:
            continue

        path = len(nx.shortest_path(G, node, kevinBacon)) - 1
    except nx.NetworkXNoPath:
        file.write("No path exists between %s and %s!\n" % (node, kevinBacon))
    else:
        if path > maxDistance:
            maxDistance = path

        sumShortestDistances += path
        numShortestDistances += 1

file.write("\nMaximum shortest path from some node to %s is %d.\n" % (kevinBacon, maxDistance))
file.write(
    "Average distance from each node to %s is %.3f.\n" % (kevinBacon, sumShortestDistances / numShortestDistances))
file.write("Degree of separation is: %.3f." % (sumShortestDistances / numShortestDistances - 1))
file.close()
