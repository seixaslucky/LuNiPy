import math
#calcula a distancia euclidiana e checa se o user esta an area do ap
class Connection(object):

    def connect(self, user, ap, config):
        dist = self.euclideanDist(user, ap)
        if(dist <= config.raio):
            return True, dist
        else:
            return False, dist 




    def euclideanDist(self, user, ap):

        #distancia² = x²+y² distancia euclidiana
        x = (user.x) - (ap.x)
        y = (user.y) - (ap.y)
        dist = math.sqrt((x**2) + (y**2))

        return dist