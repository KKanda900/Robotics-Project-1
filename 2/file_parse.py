from robot import Robot

def parse_problem(world_file, problem_file):
    line_counter = 0
    robot = None
    obstacle_pts = []
    
    with open(world_file) as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(' ')
            if line_counter == 0:
                length = 0
                width = 0
                for i in range(len(line)):
                    if i == 0:
                        length = float(line[i])
                    elif i == 1:
                        width = float(line[i])
                robot = Robot(width, length)

            else:
                obstacle_one = []
                for pt in line:
                    obstacle_one.append(float(pt))
                obstacle_pts.append(obstacle_one)

            line_counter += 1

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

    start = None
    goal = None
    
    with open(problem_file) as f:
        for line in f:
            line = line.replace('\n', '')
            line = line.split(' ')
            start = (float(line[0]), float(line[1]), float(line[2]))
            goal = (float(line[3]), float(line[4]), float(line[5]))

    return (robot, obstacle_pts, start, goal)