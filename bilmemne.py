import matplotlib.pyplot as plt
import numpy as np

class ATuyg:
    
    def __init__(self, model_name):
        self.model_name = model_name
        self.a = 10
        self.b = 2
        self.c = 5
        self.d = 5
    
    def denge_noktalari(self):
        self.P = (self.a + self.c) / (self.b + self.d)
        self.Qd = self.a - self.b * self.P
        self.Qs = -self.c + self.d * self.P
        print("Model: {}, price: {:5.2f}, Quantitiy: {:5.2f}".format(self.model_name, 
                                                                     self.P, self.Qd))
        
    def talep_grafigi(self):
        self.denge_noktalari()
        
        price = np.linspace(0, self.a/self.b)
        quantitiy_d = self.a - self.b*price
        
        yatay_x = [0, self.Qd]
        yatay_y = [self.P, self.P]
        dikey_x = [self.Qd, self.Qd]
        dikey_y = [0, self.P]


               
        fig, ax = plt.subplots()   #Bu aşamada Çalıştır
        ax.set_xlabel("Quantitiy", fontsize = 10, fontweight = "bold")
        ax.set_ylabel("Price", fontsize = 10, fontweight = "bold")
        ax.set_title("{}: Demand Graph".format(self.model_name),
                    fontsize= 14, fontweight = "bold")
        ax.set_xlim(0, self.a*1.1)
        ax.set_ylim(0, self.a / self.b*1.1) 
        
        ax.plot(quantitiy_d, price, "k-")
        ax.plot(yatay_x, yatay_y,"r--o",
               dikey_x, dikey_y, "r--o")
        
    def arz_grafigi(self):
        
        self.denge_noktalari()
        
        price = np.linspace(0, self.a/ self.b)
        quantitiy_s = -self.c + self.d*price
        
        yatay_x = [0, self.Qd]
        yatay_y = [self.P, self.P]
        dikey_x = [self.Qd, self.Qd]
        dikey_y = [0, self.P]

        fig, ax = plt.subplots()
        ax.set_xlabel("Quantitiy", fontsize = 10, fontweight = "bold")
        ax.set_ylabel("Price", fontsize = 10, fontweight = "bold")
        ax.set_title("{}: Supply Graph".format(self.model_name),
                    fontsize= 14, fontweight = "bold")
        ax.set_xlim(0, self.a*1.1)
        ax.set_ylim(0, self.a / self.b*1.1)
        
        ax.plot(quantitiy_s, price, "k-")
        ax.plot(yatay_x, yatay_y,"r--o",
               dikey_x, dikey_y, "r--o")
        
    def piyasa_grafigi(self):
        
        self.denge_noktalari()
        
        price = np.linspace(0, self.a/ self.b)
        quantitiy_d = self.a - self.b*price
        quantitiy_s = -self.c + self.d*price
        
        yatay_x = [0, self.Qd]
        yatay_y = [self.P, self.P]
        dikey_x = [self.Qd, self.Qd]
        dikey_y = [0, self.P]

        fig, ax = plt.subplots()
        ax.set_xlabel("Quantitiy", fontsize = 10, fontweight = "bold")
        ax.set_ylabel("Price", fontsize = 10, fontweight = "bold")
        ax.set_title("{}: Market Equilibrium Graph".format(self.model_name),
                    fontsize= 14, fontweight = "bold")
        ax.set_xlim(0, self.a*1.1)
        ax.set_ylim(0, self.a / self.b*1.1)
        
        ax.plot(quantitiy_s, price, "k-",
               quantitiy_d, price, "k-")
        ax.plot(yatay_x, yatay_y,"r--o",
               dikey_x, dikey_y, "r--o")
        
        ax.annotate("Q: {:5.2f}, P: {:5.2f}".format(self.Qd, self.P),
                   xy = (self.Qd*1.05, self.P/1.05))
        
m1 = ATuyg("Model1")
m1.piyasa_grafigi()
        
m2 = ATuyg("Model2")
m2.a = m2.a*1.4
m2.piyasa_grafigi()       

plt.show()