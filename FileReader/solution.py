class FileReader:
    def __init__(self, url):
        self.url = url
    def read(self):
        try:
            with open(self.url, 'r') as file:
                return(file.read())
        except FileNotFoundError:
            return ''