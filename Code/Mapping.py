from User import User
from Connection import Connection
import numpy as np
from PowerReceived import PowerReceived
from Sinr import Sinr

class Mapping(object):

    def mapPowerSinr(self, aps, config):
        user = User('m',0,0)
        pot = []
        connection = Connection()
        calcP = PowerReceived()
        calcS = Sinr()
        

        max_y = (config.lim_max_y)*config.h_map_scale
        max_x = (config.lim_max_x)*config.h_map_scale

        powers = np.zeros(shape = (max_y, max_x))
        sinrs = np.zeros(shape = (max_y, max_x))
        for i in range(0, max_y):
            user.y = i/config.h_map_scale
            
            for j in range(0, max_x):
                
                user.x = j/config.h_map_scale


                potencias = []
                #percorre os aps e identifica se o usuario esta no range
                for k in range(0, len(aps)):
                    dist_euclidean = 0 
                    hip= 0
                    p =0
                    
                    dist_euclidean = connection.euclideanDist(user, aps[k])
                    #checa se usuario esta no range do ap, calcula a potencia e distancia 
                    
                    p, hip = calcP.calcPower(config,dist_euclidean)
                    potencias.append(p)
                
                
                position = potencias.index(max(potencias))
                potaux = potencias[position]
                powers[i][j] = calcP.converter(potaux)
                
                potencias.remove(potencias[position])
                soma_potencias = 0
                soma_potencias = sum(potencias)

                sinrs[i][j] = calcS.calcSinr(config, potaux, soma_potencias)
        

                
        return powers, sinrs
