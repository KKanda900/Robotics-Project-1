from tree import Tree
from sample import sample

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

    return (st.return_path(st.root, goal))[::-1]