__all__ = ['XMLChunk']


class XMLChunk():
    chunk = None

    def __init__(self):
        self.chunk = ''

    def add(self, s, a = None):
        if a:
            print('We should also add Attributes...')
        self.chunk += s

    def get(self):
        return self.chunk

    def reset(self):
        _c = self.chunk
        self.chunk = ''
        return _c
