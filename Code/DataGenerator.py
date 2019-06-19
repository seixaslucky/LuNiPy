from Movement import Movement
from Connection import Connection
from Data import Data
from Sinr import Sinr
from PowerReceived import PowerReceived
from Ber import Ber

class DataGenerator(object):

    #recebe os usuarios e aps, e chama as classes para movimentar e calcular e conectar
    def createData(self, aps,config, users):
        move = Movement()
        d = []
        connection = Connection()
        s = Sinr()
        power = PowerReceived()

        ap_principal = None
        distancia_principal = None
        power_principal = None
        cber = Ber()
        
        
        
        
        #percorre os usuarios move um a um
        for i in range(0, len(users)):
            flag = False
            users[i] = move.move(config, users[i])
            p=0
            potencias = []
            aps_lista = []
            distancias = []
            #percorre os aps e identifica se o usuario esta no range
            for j in range(0, len(aps)):
                
                dist_euclidean = connection.euclideanDist(users[i], aps[j])
                #checa se usuario esta no range do ap, calcula a potencia e distancia 
                
                aps_lista.append(aps[j])
                p, hip = power.calcPower(config,dist_euclidean)
                    
                distancias.append(dist_euclidean)
                potencias.append(p)
                
                    
                    
            data = None
            #se o ap esta conectado ao usuario, adiciona a uma lista de objedots dados
            
            #distancia_principal = min(distancias)
            power_principal = max(potencias)

            position = potencias.index(power_principal)
                
            ap_principal = aps_lista[position]

            distancia_principal = distancias[position]
                
            aps_lista.remove(aps_lista[position])
            distancias.remove(distancias[position])
            potencias.remove(potencias[position])
                
            soma_potencias = 0
            soma_potencias = sum(potencias)
               
            sinr = s.calcSinr(config, power_principal, soma_potencias)

            ber = cber.calcBer(config, sinr)

            data = Data(users[i],aps,ap_principal,distancias,distancia_principal, potencias, power.converter(power_principal),sinr, ber)
                
            
            d.append(data)
        #retorna os usuarios em suas novas posicoes e a listas dos dados de conexao
        return d, users