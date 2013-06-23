import json
from networkx.readwrite import json_graph
import networkx as nx
G=nx.Graph()

pruned = open('PRUNED.txt', 'r')

links = []
nodes = []
for line in pruned:
    source, target = line.split(" -> ")
    source = source.strip()
    target = target.strip()
    G.add_edge(source.strip(),target.strip())
    #G.add_edges_from([(source,target,{'color':'blue'}), (2,3,{'weight':8})])

G.remove_edge("Carnivora", "Caniformia")
nodes = nx.shortest_path(G,'Caniformia').keys()
G2 = G.subgraph(nodes)
#"Feliformia" -> "Carnivora" -> "Caniformia"
d = json_graph.node_link_data(G2)
json.dump(d, open('force.json','w'))
import pdb; pdb.set_trace()
