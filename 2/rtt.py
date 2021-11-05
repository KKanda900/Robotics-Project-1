from tree import Tree
from sample import sample

def rtt(robot, obstacles, start, goal, iter_n):
    st = Tree(robot, obstacles, start, goal)

    for n in range(iter_n):
        q_rand = sample()
        q_nearest = st.nearest(q_rand)
        print("q_rand and q_nearest: ", q_rand, q_nearest)
        if st.extends(q_rand, q_nearest):
            st.add(q_rand, q_nearest)

    if st.extends(st.nodes[len(st.nodes)-1], goal):
        st.add(st.nodes[len(st.nodes)-1], goal)

    return (st.return_path(st.root, goal))[::-1]