from matplotlib.transforms import Affine2D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D
import random

def check_intersection(polygon1, polygon2):
    poly1 = Polygon(polygon1)
    poly2 = Polygon(polygon2)
    return poly1.contains(poly2)
    #return not set(map(lambda x: frozenset(tuple(x)), polygon1)).isdisjoint(set(map(lambda x: frozenset(tuple(x)), polygon2)))

# fix this to better suit what we need
def linesIntersection(A, B, C, D):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    
    x3 = C[0]
    y3 = C[1]
    x4 = D[0]
    y4 = D[1]
    
    #print x1, y1, x2, y2
    #print x3, y3, x4, y4
    
    denomenator = (((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4)))
    
    if denomenator != 0:
        P1 = (((x1*y2 - y1*x2)*(x3-x4)) - ((x1-x2)*(x3*y4-y3*x4)))
        Px = P1 / denomenator
        
        P2 = (((x1*y2 - y1*x2)*(y3-y4)) - ((y1-y2)*(x3*y4-y3*x4)))
        Py = P2 / denomenator
    else:
        return None
    
    print("The Intersection points are: ", Px, Py)
    return (Px, Py)

# check the segments of robot compared to the obstacle and (maybe check the center of mass distance between both polygons)
def intersection(robot, obstacle):
    robot = robot.append(robot[len(robot)-1])
    obstacle = obstacle.append(obstacle[len(obstacle)-1])

    robotSegments = []
    obstacleSegments = []

    for i in range(len(robot)):
        if i+1 <= len(robot)-1:
            robotSegments.append([robot[i], robot[i+1]])

    for i in range(len(obstacle)):
        if i+1 <= len(obstacle)-1:
            obstacleSegments.append([obstacle[i], obstacle[i+1]])

    while len(robotSegments) != 0:
        robot_seg = robotSegments.pop(0)
        for i in range(len(obstacleSegments)):
            if linesIntersection(robot_seg[0], robot_seg[0], obstacleSegments[i][0], obstacleSegments[i][1]) != None:
                return True

    return False


def isCollisionFree(robot, point, obstacles):
    robot_pts = translate_robot(robot, point)

    ''' for i in range(len(robot_pts)):
        if robot_pts[i][0] < 0 and robot_pts[i][1] < 0:
            return False
        elif robot_pts[i][0] > 10 and robot_pts[i][1] > 10:
            return False '''

    for i in range(len(obstacles)):
        obstacles_pts = obstacles[i]
        if intersection(robot_pts, obstacles_pts) == True:
            return False

    return True

def visualize_robot(robot, point):
    #og = Polygon(robot, facecolor='r')
    robot = translate_robot(robot, point)
    p = Polygon(robot, facecolor='k')

    fig,ax = plt.subplots()

    #ax.add_patch(og)
    ax.add_patch(p)

    ax.set_xlim([0,10])
    ax.set_ylim([0,10])

    plt.show()
    

def inside_polygon(point, obstacle):
    x = point[0]
    y = point[1]

    inside = False
    for i, j in zip(range(len(obstacle))):
        pass

def translate_robot(robot, point):
    transformation_matrix = np.array([[1, 0, point[0]], [0, 1, point[1]], [0, 0, 1]])
    new_robot = []
    for i in range(len(robot)):
        #coord_vector = np.array([[robot[i][0]], [robot[i][1]], [1]])
        robot_pt = [robot[i][0]+point[0], robot[i][1]+point[1]]
        new_robot.append(robot_pt)

    ''' for i in range(len(new_robot)):
        new_robot[i] = list(new_robot[i]) '''

    #print(new_robot)

    return new_robot