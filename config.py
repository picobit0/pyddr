import yaml

asciiFormats = ("none", "tree", "list")
repositoryModes = ("local", "url")

class ConfigError (Exception):
    pass

class Config ():
    def __init__ (self, config):
        self.version = str(config.get("version", ""))
        if self.version != "0.2":
            raise ConfigError(f"Unsupported config version ({self.version})")

        
        self.packageGroup = config.get("package-group", "")
        if not self.packageGroup:
            raise ConfigError(f"No package group specified")
        
        self.packageName = config.get("package-name", "")
        if not self.packageName:
            raise ConfigError(f"No package name specified")

        self.packageVersion = str(config.get("package-version", ""))
        if not self.packageVersion:
            raise ConfigError(f"No package group specified")
        
        self.repo = config.get("repository-path", "repo.txt")

        self.mode = config.get("repository-mode", "local")
        if not self.mode in repositoryModes:
            raise ConfigError(f"Unknown repository mode: {self.mode}")
        
        self.output = config.get("output-path", "output.png")
        if not isinstance(self.output, str):
            raise ConfigError(f"Wrong output path: {self.output}")
        
        self.ascii = config.get("ascii-format", "none")
        if not self.ascii in asciiFormats:
            raise ConfigError(f"Unknown ascii format: {self.ascii}")
        
        self.depth = config.get("max-depth", 15)
        if not isinstance(self.depth, int) or self.depth <= 0:
            raise ConfigError(f"Invalid max depth: {self.depth}")

    @property
    def packageInfo (self):
        return self.packageGroup, self.packageName, self.packageVersion

    @property
    def repoInfo (self):
        return self.repo, self.mode

    @staticmethod
    def from_file (path):
        try:
            with open(path, encoding="utf-8") as f:
                configDict = yaml.load(f, yaml.Loader)
            res = Config(configDict)
            return res
        except FileNotFoundError:
            raise ConfigError(f"Can't open config file: {path}")
        except yaml.scanner.ScannerError:
            raise ConfigError(f"Config file is not a valid yaml file")
            
    def print (self):
        print("Version:", self.version)
        print("Package group:", self.packageGroup)
        print("Package name:", self.packageName)
        print("Package version:", self.packageVersion)
        print("Repository path:", self.repo)
        print("Repository mode:", self.mode)
        print("Output path:", self.output)
        print("Ascii format:", self.ascii)
        print("Max depth:", self.depth)
