from xml.etree.ElementTree import ElementTree
from urllib.request import urlopen
from urllib.error import HTTPError

class PackageFetchError (Exception):
    pass

def strip_tag_prefix (tag):
    return tag.split("}")[-1]

def xml_to_dict (element):
    tag = strip_tag_prefix(element.tag)
    if not len(element):
        return {
            tag: (element.text or "").strip()
        }
    
    children = {}
    for child in element:
        childDict = xml_to_dict(child)
        if type(children) == dict:
            if children.keys() & childDict.keys():
                children = list(children.values())
            else:
                children.update(childDict)
        if type(children) == list:
            children += list(childDict.values())
    return {
        tag: children
    }    

def read_variables (pom):
    res = pom.get("properties", {})
    if "version" in pom:
        res["project.version"] = pom["version"]
    return res

def unpack_vars_in_string (s, variables):
    res = ""
    pos = 0
    while True:
        st = s.find("${", pos)
        end = s.find("}", st)
        if st == -1 or end == -1:
            res += s[pos:]
            break
        res += s[pos:st]
        var = s[st+2:end]
        if var in variables:
            res += variables[var]
        else:
            res += "{??" + var + "??}"
        pos = end + 1
    return res

def unpack_vars_in_dict (d, variables):
    if type(d) == dict:
        it = d
    else:
        it = range(len(d))
    for k in it:
        if type(d[k]) == str and "$" in d[k]:
            d[k] = unpack_vars_in_string(d[k], variables)
        if not type(d[k]) == str:
            unpack_vars_in_dict(d[k], variables)

class MavenPackage:
    def __init__ (self, group, id, version):
        self.group = group
        self.id = id
        self.version = version
        
        self._pom = None
        self._variables = None

    def get_relative_url (self):
        group = self.group.replace(".", "/")
        return f"{group}/{self.id}/{self.version}/{self.id}-{self.version}.pom"

    def fetch_data_from_repo (self, repoPath, mode):
        if mode == "local":
            self.fetch_data_from_local_repo(repoPath)
        elif mode == "url":
            self.fetch_data_from_remote_repo(repoPath)

    def fetch_data_from_local_repo (self, repoPath):
        path = repoPath + self.get_relative_url()
        tree = ElementTree()
        with open(path) as f:
            pom = tree.parse(f)
        self._parse_pom(pom)
    
    def fetch_data_from_remote_repo (self, repoUrl):
        url = repoUrl + self.get_relative_url()
        tree = ElementTree()
        try:
            with urlopen(url) as r:
                pom = tree.parse(r)
        except HTTPError as err:
            raise PackageFetchError(f"Couldn't fetch from '{url}' - {err}")
        self._parse_pom(pom)
    
    def _parse_pom (self, pom):
        self._pom = xml_to_dict(pom)["project"]
        self._variables = read_variables(self._pom)
        unpack_vars_in_dict(self._pom, self._variables)

    def get_dependency_list (self):
        if self._pom is None:
            raise Exception("Package data should be fetched from repo first")

        res = []
        dependencies = self._pom.get("dependencies", [])
        if len(dependencies) == 1:
            dependencies = dependencies.values()
        for dep in dependencies:
            version = dep.get("version", "")
            if not version or "??" in version + dep["groupId"]:
                continue
            res.append(MavenPackage(dep["groupId"], dep["artifactId"], version))
        return res
            
    def __repr__ (self):
        return f"MavenPackage({self.group}/{self.id} - {self.version})"

    def __eq__ (self, other):
        return (self.group, self.id, self.version) == (other.group, other.id, other.version)

    def __hash__ (self):
        return hash((self.group, self.id, self.version))
