import matplotlib.pyplot as plt
import base64 
from io import BytesIO
from .SuppyDemand import ATuyg

################################ FIXED FUNCTION ################################################################
def get_graph():
    
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph 
################################ FIXED FUNCTION ################################################################


################################ Graphic Edit Area ##############################################################

def get_plot(x,y,z,w):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,4))
    plt.title("MARKET EQUILIBRIUM",fontsize=15)
    plt.plot(x,y,z,w)
    plt.plot([0,5,5], [10,10,0], "r--o")
    plt.xticks(rotation=45)
    plt.xlabel('Quantity',fontsize=30)
    plt.ylabel('Price', fontsize=30)
    plt.tight_layout()
    graph=get_graph()
    return graph

                                            
                                                    
                                                    
                                                    #
############################## Market Equ Variables ############################################################
demand_=ATuyg("Demand Graph")
supply=ATuyg("Supply Graph")                        
market=ATuyg("Market")

P = (market.a + market.c) / (market.b + market.d)
Qd = (market.a - market.b * P)
Qs = -market.c + market.d * P
###########################################################################################################

                                                


######################################## Demand, Supply, Market Graphs Funcs ##############################

def get_demand(quantity_d,price,yx,yy,dx,dy):
    
    fig,ax=plt.subplots()
    ax.set_xlabel("Quantity",fontsize=10,fontweight="bold")
    ax.set_ylabel("Price",fontsize=10,fontweight="bold")
    ax.set_title("{}".format(demand_.model_name),fontsize=14,fontweight="bold")
    ax.set_xlim(0,demand_.a*1.1)
    ax.set_ylim(0,demand_.a/demand_.b*1.1)
    ax.plot(quantity_d,price,"k-")  
    ax.plot(yx,yy,"r--",dx,dy,"r--")
    graph=get_graph()
    return graph

def get_supply(quantity_s,price,yx,yy,dx,dy):
    
    fig, ax = plt.subplots()
    ax.set_xlabel("Quantitiy", fontsize = 10, fontweight = "bold")
    ax.set_ylabel("Price", fontsize = 10, fontweight = "bold")
    ax.set_title("{}".format(supply.model_name), fontsize= 14, fontweight = "bold")
    ax.set_xlim(0, supply.a*1.1)
    ax.set_ylim(0, supply.a / supply.b*1.1)
    ax.plot(quantity_s,price,"k-")
    ax.plot(yx,yy,"r--",dx,dy,"r--")
    graph=get_graph()
    return graph

def get_market(quantity_s,price,quantity_d,yx,yy,dx,dy):
    
    fig, ax = plt.subplots()
    ax.set_xlabel("Quantitiy", fontsize = 10, fontweight = "bold")
    ax.set_ylabel("Price", fontsize = 10, fontweight = "bold")
    ax.set_title(" {} Equilibrium Graph".format(market.model_name),
                    fontsize= 14, fontweight = "bold")
    ax.set_xlim(0, market.a*1.1)
    ax.set_ylim(0, market.a / market.b*1.1)
        
    ax.plot(quantity_s, price, "k-",quantity_d,price, "k-")

    ax.plot(yx, yy,"r--o",dx, dy, "r--o")
        
    ax.annotate("Q: {:5.2f}, P: {:5.2f}".format(Qd, P),
                   xy = (Qd*1.05, P/1.05))

    graph=get_graph()
    return graph


############################################################################################################







    
    


