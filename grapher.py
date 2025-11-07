from argparse import ArgumentParser
from config import Config, ConfigError
from maven_package import MavenPackage, PackageFetchError
from graph_builder import build_graph
from graph_renderer import render_graph, print_as_tree

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
        if config.ascii == "none":
            print("Rendering graph...")
            render_graph(graph, config.output, f"Dependencies of {rootPackage}")
            path = config.output + ("" if config.output.endswith(".svg") else ".svg")
            print(f'Done! File saved at "{path}"')
        elif config.ascii == "list":
            print("\n=== Dependency list ===")
            for package in graph:
                print(f"{package}:")
                for d in (graph[package] or [""]):
                    print("-", d)
                print()
        elif config.ascii == "tree":
            print("\n=== Dependency tree ===")
            print_as_tree(graph)
    except ConfigError as err:
        print("Error!", err)
    except PackageFetchError as err:
        print(err)
