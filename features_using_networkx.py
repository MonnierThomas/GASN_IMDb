import networkx as nx
import glob

def get_features():
    dataset = []
    for filename in glob.glob('Moviegalaxies dataset. Jermain Kaminski. 2018/dataset versión harvard/gexf/gexf/*.gexf'): #assuming gexf
        graph = nx.read_gexf(filename)
        dataset.append([int(filename.split('\\')[1].split(".")[0]), graph.number_of_edges(), graph.number_of_nodes(), list(nx.betweenness_centrality(graph).values()), list(nx.eccentricity(graph).values()), list(nx.closeness_centrality(graph).values()), list(dict(graph.degree()).values())])
    return sorted(dataset)