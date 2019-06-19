import math
#calcula o signal inteference noise ratio
class Sinr(object):

    def calcSinr(self, config, power_principal, soma):


        omega = self.omega(config,power_principal)
       
        sinr = math.pow(power_principal, 2)/(omega + soma )
        sinr = self.converter(sinr)
        return sinr



    def omega(self, config, power_principal):
        #omegatotal: Visible Light Communication, Networking, and Sensing- A Survey, Potential and Challenges (3)
        
        shot_p1 = 2*config.q*power_principal*config.noise_bandwith
        shot_p2 = 2*config.q*config.back_current*config.idois*config.noise_bandwith
        omegaShot= shot_p1 +shot_p2
        
        
        thermal_p1= (8*math.pi*config.k*config.absolute_temp)/config.gol
        thermal_p2= config.pd_capacitance*config.receiver_area*config.idois*config.noise_bandwith
        thermal_p3= (16*math.pow(math.pi,2)*config.k*config.absolute_temp*config.noise_factor)/config.fet_m
        thermal_p4= config.pd_capacitance*math.pow(config.receiver_area,2)*config.itres*math.pow(config.noise_bandwith,3)
        
        omegaThermal = (thermal_p1*thermal_p2)+(thermal_p3*thermal_p4)
        
        
        
        #omegaShot = 2*config.q*config.responsivity*config.noise_bandwith*config.noise_factor
        #omegaThermal = math.pow(10,-15)
        omegaTotal = omegaThermal+omegaShot
        return omegaTotal
    
    def converter(self, mW):
        #This function converts a power given in mW to a power given in dBm.
        return 10.*math.log10(mW)
