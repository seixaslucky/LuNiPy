from User import User
from Ap import Ap
import random
import time

#cria usuarios
class FactoryUser(object):


    def createUsers(self, config):
        users = []

            #random das posicoes
        for i in range(0, config.num_users):
            random.seed(time.time())
            val_x = random.uniform(config.lim_min_x, config.lim_max_x)
            random.seed(time.time())
            val_y = random.uniform(config.lim_min_y, config.lim_max_y)

            #preenche a lista dos users
            users.append(User(i, val_x, val_y))

        return users