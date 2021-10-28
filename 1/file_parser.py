import numpy as np

def parse_problem(world_file, problem_file):
    line_counter = 0
    robot_pts = []
    obstacle_pts = []

    with open(world_file) as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(' ')
            if line_counter == 0:
                for pt in line:
                    robot_pts.append(float(pt))

            else:
                obstacle_one = []
                for pt in line:
                    obstacle_one.append(float(pt))
                obstacle_pts.append(obstacle_one)

            line_counter += 1

    x = []
    y = []
    for i in range(len(robot_pts)):
        if i % 2 == 0:
            x.append(robot_pts[i])
        else:
            y.append(robot_pts[i])

    robot_pts = []
    for i in range(len(x)):
        robot_pts.append([x[i], y[i]])

    for i in range(len(obstacle_pts)):
        x = []
        y = []
        for j in range(len(obstacle_pts[i])):
            if j % 2 == 0:
                x.append(obstacle_pts[i][j])
            else:
                y.append(obstacle_pts[i][j])

        obstacle_pts[i] = []
        for k in range(len(x)):
            obstacle_pts[i].append([x[k], y[k]])

    with open(problem_file) as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(' ')
            start = (float(line[0]), float(line[1]))
            goal = (float(line[2]), float(line[3]))

    return (robot_pts, obstacle_pts, start, goal)
