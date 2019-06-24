### mapping nodes from neo4j
import copy
from py2neo import Graph
import pandas as pd
database = Graph("http://54.169.129.170:7474", password= "0neintegral@123")
ent = database.run("match (a:GROUP_COMPANY)<-[*1]-(b) return b.name as Entities").to_data_frame()
print(ent)
index=int(input("enter the index of entity:"))
find=ent.Entities[index]
print("searching nodes for entity %s" %find)
subnodes=database.run("match p=(a)<-[*1..]-(b) where a.name={x}   with b match (b)-[r]-(c) return b as NOde,r as RElationship, c as PArent; ",x=find).to_data_frame()
##DRAWING_GRAPH
import networkx as nx
G=nx.Graph()
for i in range (len(subnodes)):
     a=subnodes.NOde[i]["name"]
     b=subnodes.PArent[i]["name"]
     r=subnodes.RElationship[i]["assign"]
     G.add_edge(a,b,assign=r)
import matplotlib.pyplot as plt
plt.figure(3,figsize=(20,20))
D=nx.draw(G,node_size=1000,with_labels=True,node_color="pink",width=2,font_weight='bold',font_size=8)
plt.show()

def ExplodeGraph(graph,node,degree):
     database = Graph("http://54.169.129.170:7474", password= "0neintegral@123")
     explodenodes = database.run("match p=(a)<-[*1..]-(b) where a.name={x} with collect(b.name) as EXPLODElist return EXPLODElist;",x=node).to_table()
     E1=list(explodenodes[0])[0]
     #print(E1)
     graphs=[graph ,]
     mapps=[0,]
     for l in range(1,degree):
          g=copy.deepcopy(graph)
          m={}
          for i in range(len(E1)):
               item=E1[i]+"_X$"+str(l)
               m[E1[i]]=item
          g_r = nx.relabel_nodes(g,mapping=m)
          graphs.append(g_r)
          mapps.append(m)
     return graphs,mapps;

opt=input("Explode graph Yes/No")
if opt =="Yes" or "Y" or "y" or "yes":
     N_list=list(G.nodes())
     print(pd.DataFrame(N_list))
     node_id=int(input("Enter the index of the node of explosion:"))
     degree=int(input("Degree of explosion"))
     node=N_list[node_id]
     graphs,mapp= ExplodeGraph(G,node,degree)
     #print(graphs)
     #print(mapp)
     GU=nx.compose_all(graphs)
     plt.figure(3,figsize=(20,20))
     D=nx.draw(GU,node_size=1000, with_labels=True,node_color="pink",width=5,font_weight='bold',font_size=8,)
     plt.show()
else:
     print("bye")
          
          
          
          








          
