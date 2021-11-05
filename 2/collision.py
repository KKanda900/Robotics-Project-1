import numpy as np
from visualizer import translate_robot

def checkIntersection(pt1, pt2, pt3, pt4):
    if (((pt1[0]-pt2[0])*(pt3[1]-pt4[1])) - ((pt1[1]-pt2[1])*(pt3[0]-pt4[0]))) != 0:
        x = ((((pt1[0]*pt2[1] - pt1[1]*pt2[0])*(pt3[0]-pt4[0])) - ((pt1[0]-pt2[0])*(pt3[0]*pt4[1]-pt3[1]*pt4[0])))) / (((pt1[0]-pt2[0])*(pt3[1]-pt4[1])) - ((pt1[1]-pt2[1])*(pt3[0]-pt4[0])))
        y = ((((pt1[0]*pt2[1] - pt1[1]*pt2[0])*(pt3[1]-pt4[1])) - ((pt1[1]-pt2[1])*(pt3[0]*pt4[1]-pt3[1]*pt4[0])))) / (((pt1[0]-pt2[0])*(pt3[1]-pt4[1])) - ((pt1[1]-pt2[1])*(pt3[0]-pt4[0])))
        return (x, y)
    else:
        return None

def distance(centroid1, centroid2):
    return np.sqrt((centroid2[0]-centroid1[0])**2 + (centroid2[1]-centroid1[1])**2)

def get_polygon_segments(polygon):
    polygon_segments = []

    for i in range(len(polygon_segments)):
        if i+1 <= len(polygon)-1:
            polygon_segments.append([polygon[i], polygon[i+1]])

    return polygon_segments

def get_xy(polygon):
    x = []
    y = []
    for i in range(len(polygon)):
        x.append(polygon[i][0])
        y.append(polygon[i][1])

    return x,y

# check the segments of robot compared to the obstacle and (maybe check the center of mass distance between both polygons)
def intersection(robot, obstacle):
    robot.append(robot[0])
    obstacle.append(obstacle[0])

    robotSegments = get_polygon_segments(robot)
    obstacleSegments = get_polygon_segments(obstacle)

    while len(robotSegments) != 0:
        robot_seg = robotSegments.pop(0)
        for i in range(len(obstacleSegments)):
            if checkIntersection(robot_seg[0], robot_seg[0], obstacleSegments[i][0], obstacleSegments[i][1]) != None:
                return True

    rx, ry = get_xy(robot)
    ox, oy = get_xy(obstacle)

    robot_centroid = (sum(rx)/len(rx), sum(ry)/len(ry)) 
    obstacle_centroid = (sum(ox)/len(ox), sum(oy)/len(oy))

    if distance(robot_centroid, obstacle_centroid) < 0.555:
        return True

    return False

def isCollisionFree(robot, point, obstacles):
    robot_pts = translate_robot(robot, point)

    for i in range(len(obstacles)):
        obstacles_pts = obstacles[i]
        if intersection(robot_pts, obstacles_pts) == True:
            return False

    return True