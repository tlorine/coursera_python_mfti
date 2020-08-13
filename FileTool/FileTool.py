import tempfile
import os.path

class File:
    def __init__(self, path):
        self.path = os.path.abspath(path)
        if os.path.exists(path) == False:
            with open(path, 'a') as f:
                pass

    def __add__(self, obj):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmpfile:
            path = os.path.join(tempfile.gettempdir(), tmpfile.name)
            tmpfile.write((self.read() + obj.read()))
            return File(path)
    
    def __iter__(self):
        with open(self.path, 'r') as file:
            self.linesList = file.readlines()
        return self
    
    def __str__(self):
        return(self.path)

    def __next__(self):
        if self.linesList:
            tmpLine = self.linesList[0]
            del self.linesList[0]
            return tmpLine
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        with open(self.path, "r") as file:
            return (file.readlines())[index]

    def write(self, text):
        with open(self.path, "w") as file:
            return (file.write(text))
    
    def read(self):
        with open(self.path, 'r') as file:
            return (file.read())