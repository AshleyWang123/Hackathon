import authentication
import random
import xml
def pickUsers(amount: int):
    users = []
    for user in authentication.usersXML.findall("user"):
        users.append(user)
        try:
            users = random.choices(users,k=amount)
            return users
        except:
            return "We couldn't find any users"
def pickEvent():
    return random.choice(xml.etree.ElementTree.parse("xml/events.xml").findall("event"))

def pickVenue():
    return random.choice(xml.etree.ElementTree.parse("xml/venues.xml").findall("venue"))
