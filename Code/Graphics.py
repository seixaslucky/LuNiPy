import matplotlib.pyplot as plt
import pylab as pl
from Mapping import Mapping
import seaborn as sns
import numpy as np
import pandas as pd
class Graphics(object):
    def plotagemPower(self, valueClean, config):
        lis_power = []
        lis_dist =[]
        fig, ax = plt.subplots()
        ax = plt.gca()
        ax.cla()
        for i in range(0, len(valueClean)):
            lis_dist.append(valueClean[i].dist)
            lis_power.append(valueClean[i].power)
            if(valueClean[i].power<= -80):
                break
        ax.set_xlim((0, config.lim_max_distancia))
        plt.plot( lis_dist, lis_power, 'go') # green bolinha
        plt.plot( lis_dist, lis_power, 'k:', color='red')
        plt.title("Power x Distance")
        plt.xlabel("Distance")
        plt.ylabel("Power")
        nome = 'powerxdistance.png'
        
        fig.savefig("./graficos/" + nome)
        plt.close()
        fig=None
    def heatMaps(self,aps, config):
        mp = Mapping()
        powers, sinrs = mp.mapPowerSinr(aps, config)
        self.heatMapPower(powers)
        self.heatMapSinr(sinrs)

        dfP= pd.DataFrame(powers)
        dfS= pd.DataFrame(sinrs)
        dfP.to_csv("./csv/power.csv")
        dfS.to_csv("./csv/sinr.csv")
        
    def heatMapPower(self, powers):
        vmin = np.amin(powers)
        vmax = np.amax(powers)


        fig, ax = plt.subplots()
        ax = plt.gca()
        ax.cla()
        
        ax = sns.heatmap(powers,cbar_kws={'label': 'dbm'},vmin=vmin,vmax=vmax,  cmap = 'RdYlGn_r', xticklabels=100, yticklabels=100)
        ax.invert_yaxis()
        ax.set_title("power heatmap")
        nome = 'heatmappotencia.png'
        fig.savefig("./graficos/" + nome)
        plt.close()
        fig=None

    def heatMapSinr(self, sinrs):
        vmin = np.amin(sinrs)
        vmax = np.amax(sinrs)
           
        fig, ax = plt.subplots()
        ax = plt.gca()
        ax.cla()
        
       
        ax = sns.heatmap(sinrs,cbar_kws={'label': 'dbm'}, vmin=vmin, vmax=vmax, cmap = 'RdYlGn_r', xticklabels=100, yticklabels=100)
        ax.invert_yaxis()
        ax.set_title("SINR heatmap")
        nome = 'heatmapSinrs.png'
        fig.savefig("./graficos/" + nome)
        plt.close()
        fig=None

 