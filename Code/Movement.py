import random
import time
from FactoryUser import FactoryUser

#recebe os usuarios e os movimenta no cenario
class Movement(object):
    def move(self, config, user):
          

        #movimento eixo x
        rand = 0
        random.seed(time.time())
        rand = random.uniform(0, 1)
        mov_x =0
        mov_x = random.uniform(0, 1)
        if rand<0.33:
            if (user.x+mov_x)<=config.lim_max_x:
                user.x = user.x + mov_x
        elif rand<0.66:
            if (user.x-mov_x)>=config.lim_min_x:
                user.x = user.x - mov_x
        else:
            pass
        #movimento eixo y
        rand = random.uniform(0,1)
        mov_y = 0
        mov_y = random.uniform(0,1)
        if rand<0.33:
            if (user.y+mov_y)<=config.lim_max_y:
                user.y = user.y + mov_y
        elif rand<0.66:
            if (user.y-mov_y)>=config.lim_min_y:
                user.y = user.y - mov_y
        else:
            pass

           
        
        return user