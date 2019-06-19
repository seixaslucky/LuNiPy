#class user
class User(object):
    id = 0
    x = 0
    y = 0

    def __init__(self, id, val_x, val_y):

        self.id = id
        self.x = val_x
        self.y = val_y