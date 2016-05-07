def bfs(s, graph):
    level = {s: 0}
    parent = {s: None}
    i = 1
    frontier = [s]  # level i - 1
    while frontier:  # stops when we run out of nodes
        print frontier
        next = []  # i moves
        for u in frontier:  # look at all nodes in frontier
            for v in graph[u]:  # look at all nodes we can reach
                if not v in level:  # have we seen this before
                    level[v] = i
                    parent[v] = u
                    next.append(v)
                # print u, v, level
        frontier = next
        i += 1
    return parent 

def shortestPath(current, end, parent, path=[]):
    if current == end:
        return path + [current]
    path.append(current)
    current = parent[current]
    return shortestPath(current, end, parent, path=path)

def main():
    graph1 = {
        'S': ['A', 'X'],
        'A': ['S', 'Z'],
        'Z': ['A'],
        'X': ['S', 'D', 'C'],
        'D': ['X', 'C', 'F'],
        'C': ['X', 'D', 'F', 'V'],
        'F': ['D', 'C', 'V'],
        'V': ['C', 'D', 'F'],
    }

    graph2 = {
        1: [2, 3, 4],
        2: [5, 6],
        5: [9, 10],
        9: [],
        10: [],
        6: [],
        3: [],
        4: [7, 8],
        7: [11, 12],
        8: [],
        11: [],
        12: [],
    }
    parent1 = bfs(1, graph2)
    start = 11
    end = 1
    path1 = shortestPath(start, end, parent1)
    print 'shortest path from %d, %d:' % (start, end)
    print path1

    parent2 = bfs('S', graph1)
    start = 'V'
    end = 'S'
    path2 = shortestPath(start, end, parent2)
    print 'shortest path from %s, %s:' % (start, end)
    print path2

if __name__ == '__main__':
    main()
