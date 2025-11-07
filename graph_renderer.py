from graphviz import Source
import os

def render_graph (graph, path, title = "Dependepncy graph"):
    path = path[:-4] if path.endswith(".svg") else path
    dot = convert_to_dot(graph, title)
    source = Source(dot)
    source.render(path, format="svg")
    os.remove(path)

def convert_to_dot (graph, title):
    res = []
    for package in graph:
        s = package.to_dot_string() + " -> {" + ",".join(d.to_dot_string() for d in (graph[package] or [])) + "}"
        res.append(s)
    title = title.replace('"', '\\"')
    return f'digraph "{title}"' + "{" + ";".join(res) + "}"

def print_as_tree (graph):
    visited = set()
    for root in graph:
        if root in visited: continue
        stack = [(root, 0)]
        lineStack = []
        while stack:
            package, depth = stack.pop()
            last = depth < 0
            if last:
                depth *= -1
            while len(lineStack) < depth:
                lineStack.append(True)
            lineStack = lineStack[:depth]
            if last:
                lineStack[depth - 1] = False
            if depth > 0:
                for i in range(depth - 1):
                    if lineStack[i]:
                        print("│ ", end = "")
                    else:
                        print("  ", end = "")
                if last:
                    print("└ ", end="")
                else:
                    print("├ ", end="")
            print(package, end="")
            
            if package not in visited or isinstance(package, str):
                visited.add(package)
                if not graph.get(package, None):
                    print()
                    continue
                stack.append((graph[package][-1], -depth - 1))
                stack.extend((d, depth + 1) for d in reversed(graph[package][:-1]))
                print(":")
            else:
                print()
                stack.append(("...", -depth - 1))
        print()
