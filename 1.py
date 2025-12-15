
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': ['C']
}


def has_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()

    if start == end:
        return True

    visited.add(start)

    for n in graph.get(start, []):
        print (n)
        if n not in visited:
            if has_path(graph, n, end, visited):
                return True

    return False


print(has_path(graph, 'A', 'E'))
print(has_path(graph, 'C', 'D'))
print(has_path(graph, 'A', 'F'))
print(has_path(graph, 'F', 'E'))
print(has_path(graph, 'E', 'A'))