import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon
from tree import Tree
from sampler import sample
from collision import translate_robot
import matplotlib.animation as animation

def visualize_problem(robot, obstacles, start, goal):
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

# fix this`
def visualize_points(points, robot, obstacles, start, goal):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0,10)
    ax.set_ylim(0,10)

    v= np.array(robot)

    patch = Polygon(v,closed=True, fc='r', ec='r')
    ax.add_patch(patch)

    def init():
        return patch,

    def animate(i):
        v = np.array(translate_robot(robot, points[i]))
        patch.set_xy(v)
        return patch,

    print(np.arange(1,5))

    ani = animation.FuncAnimation(fig, animate, np.arange(0, len(points)), init_func=init,
                                interval=1000, blit=True)
    plt.show()

def visualize_path(robot, obstacles, path):
    fig,ax = plt.subplots()

    p1 = Polygon(robot, facecolor='k')
            
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

def visualize_configuration(robot, obstacles, start, goal):
    pass

def visualize_rrt(robot, obstacles, start, goal, iter_n):
    fig,ax = plt.subplots()

    st = Tree(robot, obstacles, start, goal)

    plt.plot(start[0], start[1])
    plt.plot(goal[0], goal[1])

    p1 = Polygon(robot, facecolor='k')
            
    for i in range(len(obstacles)):
        p = Polygon(obstacles[i], facecolor='r')
        ax.add_patch(p)   

    ax.add_patch(p1)

    rtt_pts = []

    for n in range(iter_n):
        q_rand = sample()
        q_nearest = st.nearest(q_rand)
        if st.extends(q_rand, q_nearest):
            st.add(q_rand, q_nearest)
            rtt_pts.append(q_rand)
            rtt_pts.append(q_nearest)

    if st.extends(st.nodes[len(st.nodes)-1], goal):
        st.add(st.nodes[len(st.nodes)-1], goal)
        rtt_pts.append(st.nodes[len(st.nodes)-1])
        rtt_pts.append(goal)

    x = []
    y = []
    for i in range(len(rtt_pts)):
        x.append(rtt_pts[i][0])
        y.append(rtt_pts[i][1])

    plt.plot(x, y)
   
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])

    plt.show()

def visualize_rrt_star(robot, obstacles, start, goal , iter_n):
    fig,ax = plt.subplots()

    st = Tree(robot, obstacles, start, goal)

    plt.plot(start[0], start[1])
    plt.plot(goal[0], goal[1])

    p1 = Polygon(robot, facecolor='k')
            
    for i in range(len(obstacles)):
        p = Polygon(obstacles[i], facecolor='r')
        ax.add_patch(p)   

    ax.add_patch(p1)

    rtt_pts = []

    for n in range(iter_n):
        x_rand = sample()
        x_nearest = st.nearest(x_rand)

        if st.extends(x_nearest, x_rand):
            st.add(x_nearest, x_rand)
            st.rewire(x_rand, 1.5)
            rtt_pts.append(x_nearest)
            rtt_pts.append(x_rand)

    if st.extends(st.nodes[len(st.nodes)-1], goal):
        st.add(st.nodes[len(st.nodes)-1], goal)
        st.rewire(goal, 1.5)
        rtt_pts.append(st.nodes[len(st.nodes)-1])
        rtt_pts.append(goal)

    x = []
    y = []
    for i in range(len(rtt_pts)):
        x.append(rtt_pts[i][0])
        y.append(rtt_pts[i][1])

    plt.plot(x, y)
   
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])

    plt.show()

    

    