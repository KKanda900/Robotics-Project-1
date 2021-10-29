class Robot:

    width = 0
    height = 0
    translation = ()
    rotation = ()
    pose = ()
    coord = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.translation = (0,0)
        self.rotation = 0
        self.pose = list(self.translation)
        self.pose.append(self.rotation)
        self.pose = tuple(self.pose)
        self.coord.append((-self.width/2, -self.height/2))
        self.coord.append((-self.width/2, self.length/2))
        self.coord.append((self.width/2, self.length/2))
        self.coord.append((self.width/2, -self.height/2))


    def set_pose(self, pose):
        self.pose = pose

    def transform(self):
        pass