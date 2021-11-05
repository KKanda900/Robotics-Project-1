from file_parse import parse_problem
from visualizer import visualize_problem, visualize_points, visualize_path
from sample import sample
from collision import isCollisionFree
from rtt import rtt
from rtt_star import rtt_star

(robot, obstacles, start, goal) = parse_problem('./robot_env_01.txt', './probs_01.txt')
print(robot.coord)
print(obstacles)
print(start)
print(goal)
print('\n\n\n')

#visualize_problem(robot, obstacles, start, goal)
print('\n\n\n')

print(sample())
print('\n\n\n')

#visualize_points([(2, 2, 35), (5,5,0)], robot, obstacles, start, goal)
print('\n\n\n')

print(isCollisionFree(robot, (1,1, 0), obstacles))
print('\n\n\n')

path = rtt(robot, obstacles, start, goal, 10)
visualize_path(robot, obstacles, path)
print(path)

path_star = rtt_star(robot, obstacles, start, goal, 10)
visualize_path(robot, obstacles, path_star)
print(path_star)


