import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon
import matplotlib.animation as animation

def translate_robot(robot, point):
    print(point)
    robot.set_pose(point)
    robot.transform()
    return robot.coord

def visualize_problem(robot, obstacles, start, goal):
    fig,ax = plt.subplots()
        
    ax.plot(start[0], start[1], 'y*')
    ax.plot(goal[0], goal[1], 'g*')

    print(start)
    robot.coord = translate_robot(robot, start)

    p1 = Polygon(robot.coord, facecolor='r')
        
    for i in range(len(obstacles)):
        p = Polygon(obstacles[i], facecolor='b')
        ax.add_patch(p)   

    ax.add_patch(p1)
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])

    plt.show()

# fix this
def visualize_points(points, robot, obstacles, start, goal):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)

    v= np.array(robot.coord)

    patch = Polygon(v,closed=True, fc='r', ec='y')
    ax.add_patch(patch)

    def init():
        return patch,

    def animate(i):
        v = np.array(translate_robot(robot, points[i]))
        patch.set_xy(v)
        return patch,


    ani = animation.FuncAnimation(fig, animate, np.arange(0, len(points)), init_func=init,
                                interval=1000, blit=True)
    plt.show()

def visualize_path(robot, obstacles, path):
    fig,ax = plt.subplots()

    p1 = Polygon(robot.coord, facecolor='k')
            
    for i in range(len(obstacles)):
        p = Polygon(obstacles[i], facecolor='r')
        ax.add_patch(p)   

    ax.add_patch(p1)

    x = []
    y = []
    for i in range(len(path)):
        x.append(path[i][0])
        y.append(path[i][1])

    plt.plot(x, y)

    ax.set_xlim([0,10])
    ax.set_ylim([0,10])

    plt.show()