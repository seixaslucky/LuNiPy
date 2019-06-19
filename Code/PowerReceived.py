import math

#calcula o path loss consequentiment a potencia recebida
class PowerReceived(object):

    def path_loss(self, distancia, config):
         #converte semi angle para radianos
        phi = ((config.phi * math.pi) / 180)

        #calculo hipotenusa
        hip = math.sqrt((math.pow(distancia, 2)) + (math.pow(config.altura_ap, 2)))

        cos_beta = config.altura_ap / hip
        cos_alfa = config.altura_ap / hip

        fov = ((config.anguloFOV * math.pi) / 180)  #graus em radiano

        voltage_gain = math.pow(config.refractive_index, 2) / math.pow((math.sin(fov)), 2)  #consentrator gain

        #lambertian emission
        m = (math.log1p(2) / math.log1p(math.cos(phi)))
        receiver_area = config.receiver_area
        filter_transmission = config.filter_transmission

        pathLoss = (((m + 1) * receiver_area) /(
            (2 * math.pi) * math.pow(hip, 2))) * cos_alfa * math.pow(
                cos_beta, m) * voltage_gain * filter_transmission

        return pathLoss, hip

    def calcPower(self, config, distancia):
        
        p_loss, hip = self.path_loss(distancia, config)
        received_power = config.responsivity*config.potencia_ap * p_loss
        #received_power = self.converter(received_power)
        return received_power, hip

    def converter(self, mW):
        #This function converts a power given in mW to a power given in dBm.
        return 10.*math.log10(mW)
