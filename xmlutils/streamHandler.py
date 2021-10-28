__all__ = ['StreamHandler']

import xml.sax
from xmlutils import XMLChunk, ToXML


class StreamHandler(xml.sax.handler.ContentHandler):
    rootElement = None
    chunkElements = []
    chunkLevel = None
    currentLevel = 0

    lastEntry = {}
    lastName = None

    xmlchunk = XMLChunk()
    toxml = ToXML()

    def __init__(self, rootElement, chunkElements, chunkLevel):
        super().__init__()
        self.rootElement = rootElement
        self.chunkElements = chunkElements
        self.chunkLevel = chunkLevel
        print(f"Starting the Class")

    def __element_is_a_chunk_element(self, el):
        return any(el == x for x in self.chunkElements) and self.currentLevel == self.chunkLevel

    def __process_attrs(self, attrs):
        ad = {}
        for a in attrs.getNames():
            ad[a] = attrs.getValue(a)

        return ad

    def startDocument(self):
        print(f"*** Starting the document ***")
        print(f"*** Root element is {self.rootElement}")

    def endDocument(self):
        print(f"*** Ending the document ***")

    def startElement(self, name, attrs):
        self.currentLevel += 1

        if self.__element_is_a_chunk_element(name):
            self.xmlchunk.reset()

        self.xmlchunk.add(self.toxml.startElement(element=name, attributes=attrs))

    def endElement(self, name):
        self.xmlchunk.add(self.toxml.endElement(name))

        if self.__element_is_a_chunk_element(name):
            print(f"*** Chunk {name}, xml = {self.xmlchunk.get()}")
            self.xmlchunk.reset()

        self.currentLevel -= 1

        if name == self.rootElement:
            raise StopIteration

    def characters(self, content):
        self.xmlchunk.add(content)
