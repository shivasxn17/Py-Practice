import networkx as nx
import matplotlib.pyplot as plt
import json

G = nx.Graph()

with open('sample_graph_node.json') as json_file:
    data = json.load(json_file)
    parent_childs = {}

    for node in data:
    	G.add_node(node["type"])

    	if "child_container" in node:
    		for child_node in node["child_container"]:
    			for child_node_json in data: 
    				if child_node_json["id"] == child_node.split("/")[1]:
	    				G.add_edge(node["type"], child_node_json["type"],weight=4)

print(list(G.nodes))
print(list(G.edges))
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()