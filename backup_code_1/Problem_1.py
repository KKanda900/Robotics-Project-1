import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon
import random
from tree import Tree

class Problem_1:

    robot_pts = []
    obstacle_pts = []
    start = None
    goal = None

    def parse_problem(self, world_file, problem_file):
        line_counter = 0

        with open(world_file) as f:
            for line in f:
                line = line.replace("\n","")
                line = line.split(' ')
                if line_counter == 0:
                    for pt in line:
                        self.robot_pts.append(float(pt))

                else:
                  obstacle_one = []
                  for pt in line:
                        obstacle_one.append(float(pt))
                  self.obstacle_pts.append(obstacle_one)

                line_counter+=1

        print(self.obstacle_pts)

        x = []
        y = []
        for i in range(len(self.robot_pts)):
            if i % 2 == 0:
                x.append(self.robot_pts[i])
            else:
                y.append(self.robot_pts[i])

        self.robot_pts = []
        for i in range(len(x)):
            self.robot_pts.append([x[i], y[i]])

        for i in range(len(self.obstacle_pts)):
            x = []
            y = []
            for j in range(len(self.obstacle_pts[i])):
                if j % 2 == 0:
                    x.append(self.obstacle_pts[i][j])
                else:
                    y.append(self.obstacle_pts[i][j])

            self.obstacle_pts[i] = []
            for k in range(len(x)):
                self.obstacle_pts[i].append([x[k],y[k]])
            
        with open(problem_file) as f:
          for line in f:
            line = line.replace('\n', '')
            line = line.split(' ')
            self.start = (float(line[0]), float(line[1]))
            self.goal = (float(line[2]), float(line[3]))     

        return (self.robot_pts, self.obstacle_pts, self.start, self.goal)  

    def visualize_problem(self, robot, obstacles, start, goal):
        fig,ax = plt.subplots()
        
        ax.plot(start[0], start[1], 'y*')
        ax.plot(goal[0], goal[1], 'g*')

        p1 = Polygon(robot, facecolor='k')
        
        for i in range(len(obstacles)):
            p = Polygon(obstacles[i], facecolor='r')
            ax.add_patch(p)   

        ax.add_patch(p1)
        ax.set_xlim([0,10])
        ax.set_ylim([0,10])

        plt.show() 

    def sample(self):
        x = float(random.uniform(1,10))
        y = float(random.uniform(1,10))
        return (x,y)

    def visualize_points(self, points, robot, obstacles, start, goal):
        for i in range(len(points)):
            fig,ax = plt.subplots()
            
            ax.plot(start[0], start[1], 'y*')
            ax.plot(goal[0], goal[1], 'g*')

            p1 = Polygon(robot, facecolor='k')
            t = mpl.transforms.Affine2D().translate(points[i][0],points[i][1])
            tra = t + ax.transData
            p1.set_transform(tra)
            
            for i in range(len(obstacles)):
                p = Polygon(obstacles[i], facecolor='r')
                ax.add_patch(p)   

            ax.add_patch(p1)
            ax.set_xlim([0,10])
            ax.set_ylim([0,10])

            plt.show() 

    def check_intersection(self, polygon1, polygon2):
       return not set(map(lambda x: frozenset(tuple(x)), polygon1)).isdisjoint(set(map(lambda x: frozenset(tuple(x)), polygon2)))

    def isCollisionFree(self, robot, point, obstacles):
        fig,ax = plt.subplots()

        p1 = Polygon(robot)
        t = mpl.transforms.Affine2D().translate(point[0],point[1])
        tra = t + ax.transData
        p1.set_transform(tra)

        robot_pts = p1.get_xy()

        for i in range(len(robot_pts)):
            if robot_pts[i][0] < 0 and robot_pts[i][1] < 0:
                return False
            elif robot_pts[i][0] > 10 and robot_pts[i][1] > 10:
                return False

        for i in range(len(obstacles)):
            p = Polygon(obstacles[i])
            obstacles_pts = p.get_xy()
            if self.check_intersection(robot_pts, obstacles_pts) == True:
                return False

        return True

p1 = Problem_1()
(robot, obstacles, start, goal) = p1.parse_problem('./robot_env_01.txt', "./probs_01.txt")
#p1.visualize_problem(robot, obstacles, start, goal)
#point = p1.sample()
points = [p1.sample(), p1.sample()]
#p1.visualize_points(points, robot, obstacles, start, goal)
print(p1.isCollisionFree(robot, p1.sample(), obstacles))

tree_search = Tree(robot, obstacles, start, goal)
tree_search.add((0.1,1.2), (3.3, 4.4))
tree_search.add((1.1,1.2), (2.2, 2.5))
tree_search.print(tree_search.root)
# print(tree_search.parent(tree_search.root.right.point))