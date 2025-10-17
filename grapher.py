import yaml
from argparse import ArgumentParser
from config import Config, ConfigError      

def parse_args ():
    parser = ArgumentParser()
    parser.add_argument("-c", "--config")
    argv = parser.parse_args()
    return argv

if __name__ == "__main__":
    configPath = parse_args().config or "config.yaml"
    try:
        with open(configPath, encoding="utf-8") as f:
            configDict = yaml.load(f, yaml.Loader)
        config = Config(configDict)
        config.print() 
    except FileNotFoundError:
        print(f"Error! Can't open config file: {configPath}")
    except yaml.scanner.ScannerError:
        print(f"Error! Config file is not a valid yaml file")
    except ConfigError as err:
        print("Error!", err)
