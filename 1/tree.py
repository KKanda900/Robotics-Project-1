from collision import isCollisionFree
import numpy as np
import math

class BSTNode:
    
    def __init__ (self, point, left, right):
        self.point = point
        self.left = left
        self.right = right

class Tree:

    robot = None
    obstacles = None
    start = None
    goal = None
    root = None
    cost = 0
    nodes = []
    path = []

    def __init__(self, robot, obstacles, start, goal):
        self.robot = robot
        self.obstacles = obstacles
        self.start = start
        self.goal = goal
        self.root = BSTNode(start, None, None)

    # pre-order traversal: parent-left-right
    '''
    Pre-order Traversal: 

    parent
    left   parent
    right  left   parent
    parent right  left
    left   left   right
    ... 

    '''
    def print(self, root):
        if root != None:
            print(root.point)
            self.nodes.append(root.point)
            self.print(root.left)
            self.print(root.right)

    def get_cost(self, point):
        ptr = self.root
        prev = None
        while ptr is not None:
            if point == ptr.point:
                ptr.point.cost = self.euclidean_distance((0, 0), ptr.point)
                return ptr.point.cost

            prev = ptr
            if point < ptr.point:
                ptr = ptr.left
            else:
                ptr = ptr.right

    def nearest_neighborhood(self, point):
        pass

    def rewire(self, point, r):
        pass

    def add_pt(self, point):
        ptr = self.root
        prev = None
        while ptr is not None:
            if point == ptr.point:
                return self.root

            prev = ptr
            if point < ptr.point:
                ptr = ptr.left
            else:
                ptr = ptr.right
            
        tmp = BSTNode(point, None, None)
        if prev == None:
            self.root = tmp
            return self.root
        if point < prev.point:
            prev.left = tmp
        else:
            prev.right = tmp
            
        
        return self.root

    def add(self, point1, point2):
        self.add_pt(point1)
        self.add_pt(point2)

    def exists(self, point):
        ptr = self.root
        prev = None
        c = 0
        while ptr is not None:
            if point == ptr.point:
                return True

            prev = ptr
            if point < ptr.point:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return False

    def children(self, point):
        ptr = self.root
        prev = None
        c = 0
        while ptr is not None:
            if point == ptr.point:
                if ptr.left == None and ptr.right != None:
                    print(ptr.right)
                    return ptr.right.point
                elif ptr.right == None and ptr.left != None:
                    return ptr.left.point
                elif ptr.left == None and ptr.right == None:
                    break
                else:
                    return (ptr.left.point, ptr.right.point)

            prev = ptr
            if point < ptr.point:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return None

    def parent(self, point):
        ptr = self.root
        prev = None
        c = 0
        while ptr is not None:
            if point == ptr.point:
                return prev.point

            prev = ptr
            if point < ptr.point:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return None

    def euclidean_distance(self, point1, point2):
        return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

    def nearest(self, point):
        ptr = self.root

        distance = self.euclidean_distance(point, ptr.point)
        coord = ptr.point

        while ptr is not None:
            if point != ptr.point:
                new_distance = self.euclidean_distance(point, ptr.point)
            
            if new_distance < distance:
                distance = new_distance
                coord = ptr.point

            if point == ptr.point:
                break

            if point < ptr.point:
                ptr = ptr.left
            else:
                ptr = ptr.right

        return coord

    # Uses point by point basis
    def isCollisionFree(self, line):
        for i in range(len(line)):
            if isCollisionFree(self.robot, line[i], self.obstacles) == False:
                return False

        return True

    def generate_points(self, point1, point2, step_size):
        points = []

        xdist = (point2[0]-point1[0])/step_size
        ydist = (point2[1]-point1[1])/step_size

        for i in range(step_size):
            x = point1[0]+i*xdist
            y = point1[1]+i*ydist
            points.append([x,y])

        points.append(point2)

        return points

    # decretized version of extends
    def extends(self, point1, point2):
        step_size = 5
        line_segment = self.generate_points(point1, point2, step_size)

        if self.isCollisionFree(line_segment):
            return True

        return False 

    # get goal node -> add to list -> get parent -> add to list -> ....
    def return_path(self, root, goal):
        if goal != self.start:
            ptr = root
            prev = None
            while ptr is not None:
                if goal == ptr.point:
                    self.path.append(goal)
                    goal = self.parent(goal)
                    self.return_path(root, goal)

                prev = ptr
                if goal < ptr.point:
                    ptr = ptr.left
                else:
                    ptr = ptr.right
        elif goal == self.start:
            self.path.append(goal)
        
        return self.path