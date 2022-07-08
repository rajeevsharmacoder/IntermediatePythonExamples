def get_median(arr):
    arr.sort()
    n = len(arr)
    return arr[((n + 1)//2) - 1]


class Graph_Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = []


def generate_route(trace_route, source, destination):
    route = []
    while trace_route.get(destination) != source:
        route.append(destination)
        destination = trace_route.get(destination)
    route.append(destination)
    route.append(source)
    return route[::-1]


def get_path_BFS(tree, source, destination):
    visited = set()
    trace_route = {}
    next_to_visit = []
    next_to_visit.append(source)
    while len(next_to_visit) > 0:
        current_node = next_to_visit.pop(0)
        for node in tree.get(current_node).adjacent:
            if node not in visited:
                visited.add(node)
                next_to_visit.append(node)
                trace_route[node] = current_node
                if node == destination:
                    return generate_route(trace_route, source, destination)
    return []


def get_min_max_med(tree, u, v):
    node_list = get_path_BFS(tree, u, v)
    node_list = [tree.get(x).data for x in node_list]
    return min(node_list) + max(node_list) + get_median(node_list)


if __name__ == "__main__":
    N, Q = list(map(int, input().split()))
    tree_data = list(map(int, input().split()))
    tree = {}
    for i in range(N):
        tree[i+1] = Graph_Node(tree_data[i])
    for i in range(N-1):
        s, d = list(map(int, input().split()))
        tree.get(s).adjacent.append(d)
        tree.get(d).adjacent.append(s)
    for _ in range(Q):
        u, v = list(map(int, input().split()))
        print(get_min_max_med(tree, u, v))
