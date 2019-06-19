
#salva as informacoes de aps e usuarios conectados(potencia, sinr,...)
class Data(object):

    user = None
    ap_principal = None
    distancia_principal = None
    power_principal = None
    sinr = None
    ber = None
    
    aps = []
    distancias = []
    potencias = []

    def __init__(self,user,aps, ap_principal, distancias, distancia_principal,potencias, power_principal, sinr, ber):

        self.user = user
        self.aps = aps
        self.ap_principal = ap_principal
        self.distancias = distancias
        self.distancia_principal = distancia_principal
        self.potencias = potencias
        self.power_principal = power_principal
        self.sinr = sinr
        self.ber = ber
