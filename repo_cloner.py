from urllib.request import urlopen
from maven_package import MavenPackage
from graph_builder import build_graph
from os import makedirs
from os.path import exists

def local_exists (package):
    return exists(path+package.get_relative_url())

def save_as_local (package):
    url = repo[0] + package.get_relative_url()
    try:
        with urlopen(url) as r:
            d = r.read()
        p = path + package.get_relative_url()
        makedirs(p[:p.rfind("/")+1], exist_ok=True)
        with open(p, "wb") as f:
            f.write(d)
    except Exception as e:
        print(package, e)


if __name__ == "__main__":
    repo = "https://repo.maven.apache.org/maven2/", "url"
    path = "tests/repo/"
    package = MavenPackage("org.junit.jupiter", "junit-jupiter-api", "6.0.0")
    graph = build_graph(package, repo, 30, exclude=local_exists)
    for package in graph:
        save_as_local(package)
