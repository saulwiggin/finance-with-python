"""
  Name     : 4375OS_09_23_binomial_tree_graph.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

import networkx as nx 
import matplotlib.pyplot as plt 
plt.figtext(0.2,0.85,"ROE=0.88")
n=2
G=nx.Graph() 
for i in range(0,n+1):     
    for j in range(1,i+2):         
        if i<n:             
            G.add_edge((i,j),(i+1,j))
            # with edges being added, nodes are created authomatically             
            G.add_edge((i,j),(i+1,j+1)) 
posG={}    #dictionary with nodes position 


for node in G.nodes():     
    posG[node]=(node[0],n+2+node[0]-2*node[1])  # write the coordinates of nodes 
nx.draw(G,pos=posG)      

plt.show()


