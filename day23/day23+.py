import time

def build_graph(connections):
    graph = {}
    for a, b in connections:
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)
    return graph


def is_group(graph, vertices):
    for v1 in vertices:
        for v2 in vertices:
            if v1 != v2 and v2 not in graph[v1]:
                return False
    return True


def find_max_group(graph):
    nodes = list(graph.keys())
    max_group = set()
    
    def expand_group(current_group, candidates):
        nonlocal max_group
        if len(current_group) > len(max_group):
            max_group = current_group.copy()
        
        for node in candidates:
            new_group = current_group.union({node})
            if is_group(graph, new_group):
                new_candidates = {c for c in candidates if c > node}
                expand_group(new_group, new_candidates)
    
    expand_group(set(), set(nodes))
    return max_group


def main():
    connections = []
    with open('input.txt', 'r') as f:
        for line in f:
            a, b = line.strip().split('-')
            connections.append((a, b))
    
    graph = build_graph(connections)
    
    max_group = find_max_group(graph)
    
    print("THE ANSWER IS:", ','.join(sorted(max_group)))


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")