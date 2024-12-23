
'''
aq,cg,yn
aq,vc,wq
co,de,ka
co,de,ta
co,ka,ta
de,ka,ta
kh,qp,ub
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn
ub,vc,wq
'''

from collections import  defaultdict
import os


def read_file(file_name):
    with open(os.getcwd() + f'/2024/Day_23/{file_name}', 'r') as file:
        contents = file.read().split('\n')
    return [(line[0] + line[1], line[3] + line[4]) for line in contents if line and '-' in line]

def create_graph(edges):
    graph = defaultdict(set)
    for u, v in edges:
        graph[v].add(u)
        graph[u].add(v)
    return graph

def has_t_start(triangle):
    return any(s.startswith('t') for s in triangle)

def common_trio(graph):
    triangles = set()
    for node in graph:
        neighbors = list(graph[node])
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                # print(graph[neighbors[j]], neighbors[j], graph[neighbors[i]])
                common = graph[neighbors[j]] & graph[neighbors[i]]
                if neighbors[j] in graph[neighbors[i]]:
                    triangle = tuple(sorted([node, neighbors[i], neighbors[j]]))
                    triangles.add(triangle)
    result = []
    for line in triangles:
        if any(line[i].startswith('t') for i in range(len(line))):
            result.append(line)
    return result


def find_largest_clique(graph):
    def greedy_clique():
        sorted_nodes = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)
        best_clique = []
        for start_node in sorted_nodes:
            current_clique = [start_node]
            for node in sorted_nodes:
                if node not in current_clique:
                    if all(node in graph[clique_node] for clique_node in current_clique):
                        current_clique.append(node)
            if len(current_clique) > len(best_clique):
                best_clique = current_clique
        return best_clique
    largest_clique = greedy_clique()
    return ','.join(sorted(largest_clique)) if largest_clique else ''

def Solution():
    file = read_file('data.txt')
    graph = create_graph(file)
    result = common_trio(graph)
    result2 = find_largest_clique(graph)
    print('Part 1:',len(result))
    print('Part 2:', result2)

if __name__ == '__main__':  
    print(Solution())