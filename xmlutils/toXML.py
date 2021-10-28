__all__ = ['ToXML']


class ToXML():

    def endElement(self, e):
        return f"</{e}>"

    def startElement(self, element, attributes):
        aStr = ''

        if attributes.getLength() > 0:
            aStr = ' '
            for a in attributes.getNames():
                aStr += f'{a}="{attributes.getValue(a)}" '

            aStr = ' ' + aStr.strip()

        return f"<{element}{aStr}>"
