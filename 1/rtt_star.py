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
        x_new = st.steer(x_nearest, x_rand)

        if st.extends(x_nearest, x_new):
            pass