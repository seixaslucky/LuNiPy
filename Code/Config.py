import math
import scipy.special
import numpy as np
# valores que podem ser mudados para a simulacao
class Config(object):
    #valores para o cenario

    #inicio e fim do grafico dados
    val_inicial_ap_x = 0.75
    val_inicial_ap_y = 0.75
    
    distancia_entre_aps_x = 1.5
    distancia_entre_aps_y = 1.5

    constMov = 0.5

    altura_ap = 2 

    ciclo = 30
    num_aps = 16
    num_users = 50

    lim_max_x = 6 
    lim_max_y = 6 
    
    lim_min_x = 0
    lim_min_y = 0
    h_map_scale = 100 #100 = scale in cm/ 1 = scale in m  (great impact on time)
    #grafico de linha potencia
    lim_max_distancia = 20 
    lim_max_power = 40

    #quanto o user anda
    intervalo = 1

    #valores Canal
    potencia_ap = 9000  #mW.

    
    anguloFOV = 70  #em graus
    refractive_index = 1.5  #refractive index / 
    phi = 60  # semi-angle at half iluminence
    receiver_area = 0.01#(5 * math.pow(10, -4))  #0.01 #Receiver aperture area m2 %detector area, ARX (or photodiode active area) (m2) ARX =  .78E-7;
    filter_transmission = 1  #filter transmission
    irradiance = 15

    #valor probabilidade erro
    error_probability = math.pow(10, -6)  #error probability*******
    w_max = 20  #total number of dimming levels*******
    w = 1  #level********
    white_noise = math.pow(10, -21)  #white noise
    dimming_factor = 0.1  #dimming factor


    #i2 e i3
    idois = 0.562
    itres = 0.0868

    #variaveis omega
    q = 1.6 * math.pow(10, -19)  #eletronic charge / q ---------
    back_current = 5100 * math.pow(10, -6)  #background current/ ib phocurrent ---------
    noise_bandwith = 100  #MHz # noise bandwhith /bandwth pd ----------
    responsivity = 0.58  #(Amper/watts) PD responsivity

    #variavel thermal
    k = 1.3806488 * math.pow(10, -23)  #constante de boltzmann's (J/k) ------------
    absolute_temp = 295  #absolut temperature (k) / tk  ----------
    pd_capacitance = 1.12  #Fixed capacitance of photo detector per unit area (u m^-2) / Cpd ----------
    gol = 10  #Open-loop voltage gain / gol --------

    noise_factor = 30  #annel noise factor / n fet chanel T ---------------

    fet_m = 30  # FET transconductance (ms) / gm ----------

    #velocidade canal
    data_rate = 100  #Data rate (Mb/s)

    # There is a function in Matlab called qfunc. qfunc(x) calculates a value larger than x standard deviations above the mean.
    #  However, there is no such function in Sicpy,
    # but we can convert error function to q function in Scipy.special
    # (http://matrivian.github.io/python/2014/12/09/q-function-using-scipy.html)
    def qfunc(self, val):

        q = lambda x: 0.5 - 0.5 * scipy.special.erf(x / np.sqrt(2))
        return q(val)