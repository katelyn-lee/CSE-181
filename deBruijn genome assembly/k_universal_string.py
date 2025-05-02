import sys
from typing import List, Dict, Iterable

def de_bruijn_kmers(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a collection of k-mers."""
    k_mers = patterns
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

def generate_binary_kmers(k:int) -> List[str]:
    """Generates all possible binary k-mers."""
    if k == 0:
        return [""]

    kmers = []
    for kmer in generate_binary_kmers(k - 1):
        kmers.append(kmer + "0")
        kmers.append(kmer + "1")

    return kmers

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

def find_path(g: Dict[str, List[str]],s: str):
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
    path, unexplored_edges = find_path(g,source)

    while len(unexplored_edges) != 0:        
        new_start = list(unexplored_edges)[0]
        #new_start = find_source(unexplored_edges)
        p = int(path.index(new_start))

        next_path, unexplored_edges = find_path(unexplored_edges,new_start)
        
        path = path[0:p] + next_path + path[p+1:]
    return path

def cycle_to_string(cycle:List[str],k:int) -> str:
    path = cycle[0]
    del cycle[0]

    for node in cycle:
        path = path + node[-1]
    n = len(path)
    path = path[0:n-k+1]
    return path

def k_universal_string(k: int) -> str:
    """Generates a k-universal circular string."""
    kmers = generate_binary_kmers(k)
    # print(kmers)

    g = de_bruijn_kmers(kmers)
    # print(g)

    cycle = eulerian_path(g)
    # print(cycle)

    string = cycle_to_string(cycle,k)
    
    return string

print(k_universal_string(3))
