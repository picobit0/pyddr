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
        package = MavenPackage(*config.packageInfo)
        graph = build_graph(package, config.repoInfo, config.depth)
        for package in graph:
            print()
            deps = graph[package]
            print(f"{package}:")
            for d in deps:
                print("-", d)
            if not deps:
                print("-")
    except ConfigError as err:
        print("Error!", err)
    except PackageFetchError as err:
        print(err)
