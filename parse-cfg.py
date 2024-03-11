from typing import *
import sys

class GraphNode:
    def __init__(self, val=None) -> None:
        self.children: List[GraphNode] = []
        self.val = val

def calc_cyclomatic_complexity(n: int, e: int, p: int = 1) -> int:
    return e - n + 2 * p

def get_independent_paths(head: GraphNode) -> Set[List[int]]:
    all_paths: List[List[int]] = []
    def dfs(node: GraphNode, path: List[GraphNode], visited: Dict[GraphNode, int]) -> None:
        if not node.children:
            all_paths.append(tuple(path))
            return

        if visited.get(node, 1) > 2:
            return

        visited[node] = visited.get(node, 1) + 1
        for child in node.children:
            dfs(child, path + [node.val], visited)
        visited[node] = visited.get(node, 1) - 1

    dfs(head, [], {})

    independent_paths = set()
    seen = set()
    for path in sorted(all_paths, key=lambda x: len(x)):
        for node in path:
            if node not in seen:
                seen.add(node)
                independent_paths.add(path)

    return independent_paths

def main():
    head: GraphNode | None = None
    num_nodes = 1
    num_edges = 0
    with open(sys.argv[1]) as f:
        cfg: Dict[int, GraphNode] = {}
        for line in f.readlines():
            line_split: List[str] = line.split()
            node: int = int(line_split[1])
            children: List[int] = list(map(int, line_split[4:-1]))

            if node not in cfg:
                cfg[node] = GraphNode(node)

            if head is None:
                head = cfg[node]

            for child in children:
                if child not in cfg:
                    cfg[child] = GraphNode(child)
                cfg[node].children.append(cfg[child])

            num_nodes += 1
            num_edges += len(children)

    print(calc_cyclomatic_complexity(num_nodes, num_edges))
    for p in get_independent_paths(head):
        print(p)



if __name__ == '__main__':
    main()
