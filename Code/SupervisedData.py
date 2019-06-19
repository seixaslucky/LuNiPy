from User import User
from PowerReceived import PowerReceived
from Sinr import Sinr
from Ber import Ber
from Connection import Connection
class SupervisedData(object):
    
    def movUser(self, config, user):
        x = user.x + config.constMov
        y = user.y + config.constMov
        return x, y

    def cleanPower(self, config, aps, user):
        cn = Connection()
        pr = PowerReceived()
        s = Sinr()
        b = Ber()
        soma = 0
        
        pdist_euclidean  = cn.euclideanDist(user, aps[0])
        power, dist = pr.calcPower(config,pdist_euclidean)
        for i in range(1, len(aps)):
            dist_euclidean  = cn.euclideanDist(user, aps[i])
            p_parcial, hip = pr.calcPower(config,dist_euclidean)
            soma += p_parcial


        sinr = s.calcSinr(config, power, soma)
        ber = b.calcBer(config,sinr)
        val = Val(pdist_euclidean,pr.converter(power),sinr,ber,user.x, user.y)
        
        return val

    def get_values(self, config, aps):
        user = User(0,config.val_inicial_ap_x, config.val_inicial_ap_y)
        lis_val = []
        flag = True
        while(flag):
            val  = self.cleanPower(config,aps, user)
            lis_val.append(val)            
            user.x, user.y = self.movUser(config,user)
            if(user.x>(config.lim_max_x) or user.y > config.lim_max_y):
                flag = False
        return lis_val
            


        
class Val(object):
    dist = None
    power = None
    sinr = None
    ber = None
    x = None
    y = None
    def __init__(self,hip, power, sinr, ber, x, y):
        self.dist = hip
        self.power = power
        self.sinr = sinr
        self.ber = ber
        self.x = x
        self.y = y





