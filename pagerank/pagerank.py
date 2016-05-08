def pagerank(graph, damping=0.85, epsilon=1.0e-8):
    inlink_map = {}
    outlink_counts = {}
    
    def new_node(node):
        if node not in inlink_map: inlink_map[node] = set()
        if node not in outlink_counts: outlink_counts[node] = 0
        print node, inlink_map[node], outlink_counts[node]
    
    for tail_node, head_node in graph:
        print tail_node, head_node
        new_node(tail_node)
        new_node(head_node)
        if tail_node == head_node: continue
        
        if tail_node not in inlink_map[head_node]:
            inlink_map[head_node].add(tail_node)
            outlink_counts[tail_node] += 1
        print  head_node, inlink_map[head_node], \
            tail_node, outlink_counts[tail_node]
        print ''
    
    all_nodes = set(inlink_map.keys())
    print all_nodes
    for node, outlink_count in outlink_counts.items():
        if outlink_count == 0:
            outlink_counts[node] = len(all_nodes)
            print node, outlink_count, outlink_counts[node] 
            for l_node in all_nodes: 
                inlink_map[l_node].add(node)
                print l_node, inlink_map[l_node]
    
    initial_value = 1 / len(all_nodes)
    ranks = {}
    for node in inlink_map.keys(): 
        ranks[node] = initial_value
    print "ranks"
    print ranks
    
    new_ranks = {}
    delta = 1.0
    n_iterations = 0
    while delta > epsilon:
        new_ranks = {}
        for node, inlinks in inlink_map.items():
            new_ranks[node] = ((1 - damping) / len(all_nodes)) + (damping * sum(ranks[inlink] / outlink_counts[inlink] for inlink in inlinks))
        delta = sum(abs(new_ranks[node] - ranks[node]) for node in new_ranks.keys())
        ranks, new_ranks = new_ranks, ranks
        n_iterations += 1
    
    return ranks, n_iterations


def main():
    graph = [
        [3,8],
        [3,10],
        [5,11],
        [7,8],
        [7,11],
        [8,9],
        [11,2],
        [11,9],
        [11,10]
    ]
    rank = pagerank(graph)
    for k, v in rank[0].items():
        print k, v
    print graph
    

if __name__ == '__main__':
    main()
