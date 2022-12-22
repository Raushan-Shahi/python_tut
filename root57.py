class Repository:
    def __init__(self):
        self.package = {}
    def add_package(self, package):
        self.package[package.name] = package
    def total_size(self):
        result = 0 
        for package in self.packages.values():
            result += size
        return result
