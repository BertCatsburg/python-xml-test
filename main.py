import xml.sax

import xmlutils



def config(which_config):
    if which_config == "movie":
        return {
            'file': "data/movie.xml",
            'rootElement': "collection",
            'chunkElements': ['movie', 'radioshow'],
            'chunkLevel': 2
        }
    if which_config == "ProductData":
        return {
            'file': "data/ProductData.xml",
            'rootElement': "ProductData",
            'chunkElements': ['Manufacturer', 'ProductLine'],
            'chunkLevel': 2
        }


if __name__ == '__main__':

    thisConfig = config('ProductData')

    parser = xml.sax.make_parser()
    parser.setContentHandler(xmlutils.StreamHandler(
        # rootElement='ProductData',
        # chunkElements=['Manufacturer', 'ProductLine'],
        # chunkLevel=2
        rootElement=thisConfig['rootElement'],
        chunkElements=thisConfig['chunkElements'],
        chunkLevel=thisConfig['chunkLevel']
    ))


    # feed the parser with small chunks to simulate
    with open(thisConfig['file'], 'r', 128) as f:  # io.DEFAULT_BUFFER_SIZE
        i = 0
        while True:
            i = i + 1
            buffer = f.read(128)
            if buffer:  # len(buffer) != 0:
                # print(f"Just read [{buffer}] with {i} and len = {len(buffer)}")
                try:
                    parser.feed(buffer)
                except StopIteration:
                    break
