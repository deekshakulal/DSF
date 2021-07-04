import networkx as nx
import matplotlib.pyplot as plt
def printGraph(triples,n):
    G = nx.Graph()
    for triple in triples:
        G.add_node(triple[0])
        #G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edge(triple[0], triple[2])
        #G.add_edge(triple[1], triple[2])
        

    pos = nx.spring_layout(G,k=50)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='seagreen', alpha=0.9,
            labels={node: node for node in G.nodes()})
    #for triple in triples:
        #edge_labels=dict([((triple[0],triple[2],),triple[1]) for u,v,d in G.edges(data=True)])
        #nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    for triple in triples:
        nx.draw_networkx_edge_labels(G,pos,edge_labels={(triple[0],triple[2]):triple[1]},font_color='red')
    
    plt.axis('off')
    plt.savefig("KG/"+n+".png", format="PNG")
    plt.draw()
    plt.pause(1)
    
# t=[['She', 'was', 'quarantined']]
# printGraph(t)