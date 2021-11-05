from file_parser import parse_problem
from tree import Tree
from rtt import rtt
from visualizer import visualize_path, visualize_rrt, visualize_points
from collision import translate_robot, visualize_robot, intersection

(robot, obstacles, start, goal) = parse_problem('./robot_env_01.txt', "./probs_01.txt")
print(robot)
print(obstacles)
print(start)
print(goal)
print('\n\n\n')

''' print(robot)

print(intersection(robot, obstacles[0])) '''

#visualize_points([(2, 2), (5, 6)], robot, obstacles, start, goal)

tree_search = Tree(robot, obstacles, start, goal)
point1 = (1.4682256265766205, 9.410916920372491)
point2 = (4.199997629938962, 6.5924876736619415)
point3 = (4.0, 6.5924876736619415)
point4 = (5.199997629938962, 7.5924876736619415)
tree_search.add(point1, point2)
tree_search.add(point3, point4)
tree_search.print(tree_search.root)
print(tree_search.exists((0.0, 0.0)))
print(tree_search.parent((5.199997629938962, 7.5924876736619415)))
print(tree_search.children((4.0, 6.5924876736619415)))
print("Nearest Coordinate {}".format(tree_search.nearest(point3)))
print(tree_search.extends((1.0, 1.0), (2.0, 2.0)))
print('\n\n\n') 

path = rtt(robot, obstacles, start, goal, 10)
print(path)
#visualize_path(robot, obstacles, path)
visualize_rrt(robot, obstacles, start, goal, 10)
#print(translate_robot(robot, (1.0, 2.0)))