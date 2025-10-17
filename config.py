from pathlib import Path
import yaml

asciiFormats = ("default",)
repositoryModes = ("local", "url")

class ConfigError (Exception):
    pass

class Config ():
    def __init__ (self, config):
        self.version = config.get("version", "0.1")
        if self.version != "0.1":
            raise ConfigError(f"Config version mismach ({self.version} != 0.1)")
        
        self.package = config.get("package-name", "Default package")
        if not isinstance(self.package, str):
            raise ConfigError(f"Package name is not a string: {self.package}")
        
        self.repo = config.get("repository-path", "repo.txt")
        if not isinstance(self.repo, str) or not Path(self.repo).is_file():
            raise ConfigError(f"Wrong repository path: {self.repo}")

        self.mode = config.get("repository-mode", "local")
        if not self.mode in repositoryModes:
            raise ConfigError(f"Unknown repository mode: {self.mode}")
        
        self.output = config.get("output-path", "output.png")
        if not isinstance(self.output, str) or not Path(self.output).is_file():
            raise ConfigError(f"Wrong output path: {self.output}")
        
        self.ascii = config.get("ascii-format", "default")
        if not self.ascii in asciiFormats:
            raise ConfigError(f"Unknown ascii format: {self.ascii}")
        
        self.depth = config.get("max-depth", 15)
        if not isinstance(self.depth, int) or self.depth <= 0:
            raise ConfigError(f"Invalid max depth: {self.depth}")  

    def print (self):
        print("Version:", self.version)
        print("Package name:", self.package)
        print("Repository path:", self.repo)
        print("Repository mode:", self.mode)
        print("Output path:", self.output)
        print("Ascii format:", self.ascii)
        print("Max depth:", self.depth)
