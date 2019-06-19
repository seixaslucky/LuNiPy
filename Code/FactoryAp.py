from Ap import Ap
import random
import time

#cria os aps
class FactoryAp(object):

    def createAps(self, config):
        aps = []
        x = config.val_inicial_ap_x
        y = config.val_inicial_ap_y
        #preenche os valores dos aps
        for i in range(0, config.num_aps):
            if (y < config.lim_max_y):
                aps.append(Ap(i, x, y))
                x = x + config.distancia_entre_aps_x
                if (x >= config.lim_max_x):
                    y = y + config.distancia_entre_aps_y
                    x = config.val_inicial_ap_x
            else:
                print("Numero de APs superior a area delimitada")
                break

        return aps