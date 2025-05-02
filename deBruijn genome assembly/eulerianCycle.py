import sys
import random
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

def form_cycle(g: Dict[int, List[int]],s: int):
    cycle = []
    current_node = s
    next_node = g[s][0] 

    while next_node != s:   #must use next rather than curr to even start while loop, but hay better way probably
        cycle.append(current_node)
        g[current_node].remove(next_node)
        if len(g[current_node]) == 0:
            del g[current_node]

        current_node = next_node
        next_node = g[current_node][0]

    #one more cycle of while loop to resolve curr and next in g
    cycle.append(current_node)
    cycle.append(next_node)
    del g[current_node][0]
    if len(g[current_node]) == 0:
        del g[current_node]

    return cycle, g

# g = {1: [2], 2: [1, 2]}
# g = {0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}
# print(form_cycle(g,0))


def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    """Constructs an Eulerian cycle in a graph.""" 
    start = list(g)[0]

    cycle, unexplored_edges = form_cycle(g,start)

    while len(unexplored_edges) != 0:
        new_start = ''
        p = float('-inf')
        for node in cycle:
            if node in list(unexplored_edges):
                p = int(cycle.index(node))
                new_start = node
                break
        next_cycle, unexplored_edges = form_cycle(unexplored_edges,new_start)
        
        cycle = cycle[0:p] + next_cycle + cycle[p+1:]
    return cycle

# g = {1: [2], 2: [1, 2]}
# g = {0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2], 5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]}
# ans = eulerian_cycle(g)
# print(ans)

