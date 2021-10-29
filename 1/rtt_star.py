from tree import Tree
from sampler import sample

'''
def rtt(robot, obstacles, start, goal, iter_n):
    st = Tree(robot, obstacles, start, goal)

    for n in range(iter_n):
        q_rand = sample()
        q_nearest = st.nearest(q_rand)
        if st.extends(q_rand, q_nearest):
            print(q_rand, q_nearest)
            st.add(q_rand, q_nearest)

    if st.extends(st.nodes[len(st.nodes)-1], goal):
        st.add(st.nodes[len(st.nodes)-1], goal)

    return (st.return_path(st.root, goal))[::-1]
'''

def rtt_star(robot, obstacles, start, goal, iter_n):
    st = Tree(robot, obstacles, start, goal)

    for n in range(iter_n):
        x_rand = sample()
        x_nearest = st.nearest(x_rand)

        if st.extends(x_nearest, x_rand):
            st.add(x_nearest, x_rand)
            st.rewire(x_rand, 1.5)

    if st.extends(st.nodes[len(st.nodes)-1], goal):
        st.add(st.nodes[len(st.nodes)-1], goal)
        st.rewire(goal, 1.5)

    """ if not st.exists(goal):
        nearest_to_goal = st.nearest(goal)
        st.rewire(goal, 1.5)
        if nearest_to_goal is None:
            return None
        path_to_goal = st.extend(nearest_to_goal, goal)
    else:
        path_to_goal = True

    path = []
    if path_to_goal:
        path = st.return_path(st.root, goal)
        return path """

    return (st.return_path(st.root, goal))[::-1]