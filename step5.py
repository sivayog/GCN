#!/usr/bin/env python
# coding: utf-8

# In[54]:


import networkx as nx
import pandas as pd 
import matplotlib.pyplot as plt
trans =pd.read_csv('/home/siva/work/New folder/iple/mydataset/map.csv' )
trans.head(30)


# In[62]:


# trans[netamt] = trns[netamt].astype(float)


# In[ ]:


zip()


# In[32]:


### mapping nodes from neo4j
import copy
from py2neo import Graph
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
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


# In[33]:


a=set(G)
s=pd.DataFrame(a)
print(s)


# In[34]:


s.dtypes


# In[ ]:





# In[ ]:





# In[56]:


for i in range(len(trans.CSV_values_s1)):
    truth=trans.CSV_values_s1[i]
    value=trans.CSV_values_s1[i]
    if value is int :
        value= trans.CSV_values_s1[i]
        truth=trans.CSV_values_s1[i]
        diff=truth-value
        G.nodes[trans.neo_header[i]]["system1"]=[value,diff,truth]
    else:
        G.nodes[trans.neo_header[i]]["system1"]=[value,truth]


# In[57]:


a=G.nodes.data()
m=pd.DataFrame(a)
print(m)


# In[74]:


a=trans.CSV_values_s1
print(a)


# In[76]:


# pd.concat([a,b],axis=1)


# In[46]:


b=trans.csv_values_s2
print(b)


# In[63]:


c=(a==b)
print(c)


# In[10]:


import pandas as pd
import networkx as nx
import networkx.algorithms.isomorphism as isomorphism
import matplotlib.pyplot as plt
trans =pd.read_csv('/home/siva/work/New folder/iple/mydataset/PO.csv')
trans.drop('Item_Id',axis=1,inplace=True)
trans.head()


# In[11]:


trans1 =pd.read_csv('/home/siva/work/New folder/iple/mydataset/GRN.csv')
trans1.drop('Item_Id',axis=1,inplace=True)
trans1.head()


# In[12]:


list_of_tuples = list(zip(trans,trans1,trans-trans1))
list_of_tuples


# In[15]:


trans1[['GRN_Id','GRN_Qty']]


# In[46]:


trans1.GRN_Id[]


# In[58]:


from py2neo import Graph


# In[59]:


database = Graph("http://54.169.129.170:7474", password= "0neintegral@123")


# In[61]:


subnodes =database.run("match p=(a:PROCESS{name:\"DOMESTIC_PURCHASE_ORDER\"})<-[*1..]-(b) with b match (b)-[r]-(c) return b.name as NOde, type(r) as REL,c.name as PArent,b.derive as DErive;").to_data_frame()
subnodes


# In[62]:


a=subnodes.DErive
print(a)


# In[63]:


import networkx as nx


# In[64]:


for i in range (len(subnodes)):
    a=subnodes.NOde[i]
    b=subnodes.PArent[i]
    r=subnodes.REL[i]
    G.add_edge(a,b,assign=r)


# In[65]:


s=list(G.nodes)


# In[66]:


s[0]


# In[75]:


data= pd.read_csv('/home/siva/work/New folder/iple/mydataset/trans.csv')
data.head()


# In[69]:


data.dtypes


# In[76]:


data.head()


# In[78]:


truth={'SYSTEMS':"ideamed", 'DOMESTIC_PURCHASE_ORDER':"POI_1", 'VENDOR_ID':"aavv33", 'PO_ITEM_01_LINEID':"ws43",
       'PO_ITEM_01_DISC_PER':44, 'PO_ITEM_01_TAXABLE_VAL':533, 'PO_ITEM_01_MATL_CODE':435,
       'PO_NO':34, 'PO_ITEM_01_TAX_PER':34, 'PO_ITEM_01_BASE_VAL':54, 'PO_HEADER':"Poi-1",
       'GRN_ITEM_01_QTY':32, 'PO_DATE':"13sep19", 'PO_ITEM_01_TAX_ID':"fs32", 'GRN_ITEM_01_RATE':21,
       'PO_ITEM_01_DISC_AMT':543, 'PO_ITEM_01_RATE':21, 'PO_ITEM_01_NET_TOT':532,
       'GRN_ITEM_01_DISC_PER':34, 'PO_ITEM_HOLDER':"aa22", 'PO_ITEM_01_QTY':43,
       'GRN_ITEM_01_PO_ITEM_LINEID':"fd43", 'PO_ITEM_01_TAX_AMT':54,
       'GRN_ITEM_01_MATL_CODE':"fse22", 'GRN_ITEM_01_TAX_PER':21}


# In[23]:


# truth={"DOMESTIC_PURCHASE":"PURCHASE_ITEMS","GRN_ITEM_$1_DISC_PER":10,"GRN_ITEM_$1_QTY":60,"GRN_ITEM_$1_RATE":10,
#       "GRN_ITEM_$1_TAX_PER":6,"PO_DATE":"18-05-2018","PO_HEADER":"Po1543","PO_ITEM_$1_BASE_VAL":350,"PO_ITEM_$1_DISC_AMT":15
#       }


# In[79]:


data.columns


# In[83]:


truth={}
for i in range(len(data.columns)):
    truth[data.columns[i]]= data[data.columns[i]][0]
    


# In[84]:


truth


# In[85]:


import numpy


# In[86]:


for i in range(len(s)):
    true=truth[s[i]]
    value=data[s[i]][0]
    print(type(value)==numpy.int64)
    if type(value) == numpy.int64:
        diff=true-value
        if diff ==0:
            err_l=0
        else:
            err_l=1
        G.nodes[s[i]][data.SYSTEMS[0]]=[true,value,err_l]
    else:
        G.nodes[s[i]][data.SYSTEMS[0]]=[true,value]


# In[87]:


G.nodes.data()


# In[88]:


import numpy

##adding truth value to the node property
for i in range(len(s)):
    true=truth[s[i]]
    value=data[s[i]][0]
    #print(type(value)==numpy.int64)
    if type(value) == numpy.int64:
        diff=true-value
        if diff ==0:
            err_l=0
        else:
            err_l=1
        G.nodes[s[i]]["name"]=s[i]
        G.nodes[s[i]][data.SYSTEMS[0]]={"TRUTH":true,"SYSTEM":value,"DIFF_T":diff,"ERR_T":err_l}
    else:
        if true == value:
            err_l=0
        else:
            err_l=1
        G.nodes[s[i]]["name"]=s[i]
        G.nodes[s[i]][data.SYSTEMS[0]]={"TRUTH":true,"SYSTEM":value,"ERR_T":err_l}

G.nodes.data()


# In[98]:


G.nodes()


# In[115]:


def derivefromexp(string1,derive):
    import regex as re
    string=string1.replace("%","*.01")
    regex=re.compile(r"\(.*\)")
    regex1=re.compile(r"[a-zA-Z0-9_$%]+")
    mo=regex.search(string)
    mo1=regex1.search(string)
    variable=mo1.group()
    exp=mo.group()
    obj=re.compile(r"([a-zA-Z0-9_$%.]+)")
    exp1=obj.sub(r"derive['\1']",exp)
    V=eval(exp1)
    return variable,V;
    #except TypeError:
     #   return None
    ##   return None
    #except AttributeError:
      #  return None


# In[92]:


L=list(G.nodes())


# In[96]:


## dictionary of variables used for evaluating expression from derive
derive={".01":.01}
for i in range(len(L)):
    item=G.nodes[L[i]]["ideamed"]["SYSTEM"]
    if type(item)==numpy.int64:
        derive[L[i]]=item
    else:
        pass
    


# In[103]:


D_table= pd.DataFrame(data=subnodes[["NOde","DErive"]]).drop_duplicates()


# In[104]:


nodes=list(set(list(subnodes["NOde"])+list(subnodes["PArent"])))


# In[105]:


nodes


# In[106]:


Derives=database.run("match (a) where a.name = {x} return a.name,a.derive;",x=nodes)


# In[107]:


Derives.data()


# In[108]:


Derive_DF=D_table.set_index("NOde")


# In[111]:


Derive_DF


# In[116]:


## getting derived values from expression 
derived={}
for i in range(len(s)):
    try:
        print(Derive_DF.DErive[s[i]])
        k,value=derivefromexp(Derive_DF.DErive[s[i]],derive)
        derived[k]=value
    except TypeError:
        pass
    except KeyError:
        pass
    except AttributeError:
        pass


# In[118]:


### adding derived value to the node
for i in range(len(s)):
    sys_value=G.nodes[s[i]]["ideamed"]["SYSTEM"]
    try:
        der_value=derived[s[i]]
        G.nodes[s[i]]["ideamed"]["DERIVED"]=der_value
        G.nodes[s[i]]["ideamed"]["DIFF_I"]=der_value-sys_value
        if der_value-sys_value == 0:
            G.nodes[s[i]]["ideamed"]["ERR_I"]=0
        else:
            G.nodes[s[i]]["ideamed"]["ERR_I"]=1
    except KeyError:
        der_value=sys_value
        G.nodes[s[i]]["ideamed"]["DERIVED"]=der_value     
        
    


# In[119]:


G.nodes.data()


# In[120]:


DICT_DF={}
for i in range(len(G.nodes)):
    key=G.nodes[s[i]]["name"]
    value=G.nodes[s[i]]["ideamed"]
    DICT_DF[key]=value


# In[121]:


DICT_DF


# In[122]:


DF=pd.DataFrame(DICT_DF)

DF


# In[ ]:




