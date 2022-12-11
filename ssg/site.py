"""

"""

from pathlib import Path


class Site():
    def __init__(self,source,dest) -> None:
        self.source = Path(source)
        self.dest = Path(dest)


    def create_dir(self,path):
        """ """
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(Parents=True,exist_ok=True)

    def build(self):
        """ """
        self.dest.mkdir(self.dest,parents=True,exist_ok=True)

        for dir in self.source.rglob("*"):
            if Path.is_dir(dir):
                self.create_dir(dir)


