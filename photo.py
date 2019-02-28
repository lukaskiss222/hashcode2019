

class Photo(object):
    def __init__(self, id, orientation, tags):
        self.id = id
        self.orient = orientation # 0 == horizontal, 1 == vertical
        self.tags = set(tags)

        self.taken = 0 # for greedy
