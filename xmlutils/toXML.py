__all__ = ['ToXML']


class ToXML():

    def endElement(self, e):
        return f"</{e}>"

    def startElement(self, element, attributes):
        aStr = ''

        if attributes.getLength() > 0:
            # print(f'We have Attribute on {element}')

            aStr = ' '
            for a in attributes.getNames():
                # print(f'Attribute = [{a}] with value [{attributes.getValue(a)}]')
                aStr += f'{a}="{attributes.getValue(a)}" '

            aStr = ' ' + aStr.strip()

        return f"<{element}{aStr}>"
