from argparse import ArgumentParser
from config import Config, ConfigError
from maven_package import MavenPackage, PackageFetchError

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
        print(f"{package}:")
        package.fetch_data_from_remote_repo(config.repo)
        deps = package.get_dependency_list()
        for i in deps:
            print("-", i)
        if not deps: print("-")
    except ConfigError as err:
        print("Error!", err)
    except PackageFetchError as err:
        print(err)
