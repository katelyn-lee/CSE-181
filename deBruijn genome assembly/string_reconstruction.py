import sys
from typing import List, Dict, Iterable

def de_bruijn_kmers(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    adjacency_list = {}
    k = len(k_mers[0])

    for pattern in k_mers:
        prefix = pattern[0:k-1]
        suffix = pattern[1:k]
        if prefix in adjacency_list:
            adjacency_list[prefix].append(suffix)
        else: 
            adjacency_list[prefix] = [suffix]

    return adjacency_list

def find_source(g: Dict[str, List[str]]) -> str:
    in_edges = []
    for node in g:
        in_edges = in_edges + (g[node])

    for node in g:
        out_deg = len(g[node])
        in_deg = in_edges.count(node)
        if out_deg > in_deg:
            return node
    
    return list(g)[0]

def find_path(g: Dict[int, List[int]],s: int):
    path = []
    current_node = s
    next_node = g[s][0] 

    while True:
        path.append(current_node)
        g[current_node].remove(next_node)
        if len(g[current_node]) == 0:
            del g[current_node]

        current_node = next_node
        if (current_node in g):
            next_node = g[current_node][0]
        else: break
    
    path.append(current_node)

    return path, g

def eulerian_path(g: Dict[str, List[str]]) -> Iterable[str]:
    """Constructs an Eulerian path in a graph."""

    source = find_source(g)
    print(source)
    path, unexplored_edges = find_path(g,source)
    print(path)
    print(unexplored_edges)

    while len(unexplored_edges) != 0:
        new_start = find_source(unexplored_edges)
        p = int(path.index(new_start))

        next_path, unexplored_edges = find_path(unexplored_edges,new_start)
        print(next_path)
        print(unexplored_edges)
        
        path = path[0:p] + next_path + path[p+1:]
    return path

def path_to_genome(path:List[str]) -> str:
    text = path.pop(0)
    if len(path[0]) == 1:
            for node in path:
                text = text + node
            return text
    else:
        for node in path:
            text = text + node[-1]
        return text

def string_reconstruction(patterns: List[str], k: int) -> str:
    """Reconstructs a string from its k-mer composition."""
    dB_graph = de_bruijn_kmers(patterns)
    print(dB_graph)
    path = eulerian_path(dB_graph)
    print(path)
    text = path_to_genome(path)
    return text
