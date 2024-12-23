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


def find_connected_triplets(graph):
    triplets = set()
    nodes = list(graph.keys())
    
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                node1, node2, node3 = nodes[i], nodes[j], nodes[k]
                if (node2 in graph[node1] and 
                    node3 in graph[node1] and 
                    node3 in graph[node2]):
                    triplet = tuple([node1, node2, node3])
                    triplets.add(triplet)
    
    return triplets


def count_triplets_with_t(triplets):
    count = 0
    for triplet in triplets:
        contains_t = False
        for computer in triplet:
            if computer.startswith('t'):
                contains_t = True
                break
        if contains_t:
            count += 1
    return count


def main():
    connections = []
    with open('input.txt', 'r') as f:
        for line in f:
            a, b = line.strip().split('-')
            connections.append((a, b))
    
    graph = build_graph(connections)
    
    triplets = find_connected_triplets(graph)
    
    result = count_triplets_with_t(triplets)
    
    print("THE ANSWER IS:", result)
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Tiempo de ejecución: {end - start:.3f} segundos")