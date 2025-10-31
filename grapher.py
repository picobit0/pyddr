from argparse import ArgumentParser
from config import Config, ConfigError
from maven_package import MavenPackage, PackageFetchError
from graph_builder import build_graph

def get_config ():
    parser = ArgumentParser()
    parser.add_argument("-c", "--config")
    argv = parser.parse_args()
    
    configPath = argv.config or "config.yaml"
    return Config.from_file(configPath)

if __name__ == "__main__":
    try:
        config = get_config()
        rootPackage = MavenPackage(*config.packageInfo)
        print("Building dependency graph...")
        graph = build_graph(rootPackage, config.repoInfo, config.depth)

        inp = input("\nEnter package to analyse: ").replace("/", " ").replace(" - ", " ").split()
        if len(inp) != 3:
            print("Wrong input format!")
            exit()
        group, name, version = inp
        package = MavenPackage(group, name, version)
        invDependencies = [p for p in graph if package in graph[p]]
        print(f"\nInverse dependensies for {package}:")
        for p in invDependencies:
            print("-", p)
        if not invDependencies:
            print("-")
    except ConfigError as err:
        print("Error!", err)
    except PackageFetchError as err:
        print(err)
