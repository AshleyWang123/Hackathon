import Disabilites
import xml
def accountForDisability(event: xml.etree.ElementTree.Element,disability: Disabilites.Disibility):
    for tag in disability.tags:
        if (tag in event.attrib['tags'].split(" ")):
            return True