import numpy as np

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
        self.coord.append((-self.width/2, self.height/2))
        self.coord.append((self.width/2, self.height/2))
        self.coord.append((self.width/2, -self.height/2))


    def set_pose(self, pose):
        self.pose = pose

    def transform(self):
        for i in range(len(self.coord)):
            self.coord[i][0] += self.pose[0]
            self.coord[i][0] = 0 + np.cos(self.pose[2]) * (self.coord[i][0]-0) - np.sin(self.pose[2]) * (self.coord[i][1]-0)
            self.coord[i][1] += self.pose[1]
            self.coord[i][1] = 0 + np.sin(self.pose[2]) * (self.coord[i][0]-0) - np.cos(self.pose[2]) * (self.coord[i][1]-0)

        return self.coord