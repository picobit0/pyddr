from queue import deque
from maven_package import PackageFetchError

def build_graph (package, repo, maxDepth = 5, exclude=None, silent=True):
    graph = {}
    failed = set()
    queue = deque([package])
    
    for depth in range(maxDepth+1):
        if not queue: break
        n = 0
        for i in range(len(queue)):
            package = queue.popleft()
            if package in graph or package in failed: continue
            if exclude is not None and exclude(package): continue
            n += 1
            try:
                package.fetch_data_from_repo(*repo)
                dependencies = package.get_dependency_list()
                graph[package] = dependencies
                queue.extend(dependencies)
            except Exception as e:
                failed.add(package)
            
        if not silent and n > 0:
            print(f"Fetched {n} package" + ("" if n%100==1 else "s") + f" (depth {depth})")

    return graph

if __name__ == "__main__":
    from maven_package import MavenPackage
    repo = "https://repo.maven.apache.org/maven2/", "url"
    repo = "tests/repo/", "local"
    package = MavenPackage("org.scala-lang", "scala3-library_3", "3.7.3")
    graph = build_graph(package, repo, 15)
