"""
  Name     : 4375OS_09_25_binomial_two_step_graph.py
  Book     : Python for Finance
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 12/26/2013
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""
import networkx as nx 
import matplotlib.pyplot as plt 
plt.figtext(0.08,0.6,"Stock price=$20")
plt.figtext(0.08,0.56,"call =7.43")

plt.figtext(0.33,0.76,"Stock price=$67.49")
plt.figtext(0.33,0.70,"Option price=0.93")
plt.figtext(0.33,0.27,"Stock price=$37.40")
plt.figtext(0.33,0.23,"Option price=14.96")

plt.figtext(0.75,0.91,"Stock price=$91.11")
plt.figtext(0.75,0.87,"Option price=0")

plt.figtext(0.75,0.6,"Stock price=$50")
plt.figtext(0.75,0.57,"Option price=2")

plt.figtext(0.75,0.28,"Stock price=$27.44")
plt.figtext(0.75,0.24,"Option price=24.56")

n=2
G=nx.Graph() 
for i in range(0,n+1):     
    for j in range(1,i+2):         
        if i<n:             
            G.add_edge((i,j),(i+1,j))
            G.add_edge((i,j),(i+1,j+1)) 
posG={}
for node in G.nodes():     
    posG[node]=(node[0],n+2+node[0]-2*node[1])
nx.draw(G,pos=posG)      
plt.show()

