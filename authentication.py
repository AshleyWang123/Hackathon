import xml.etree.ElementTree as Tree
import hashlib
import Disabilites
usersFile = open("xml/users.xml","a+")
usersXML = Tree.ElementTree()
try:
    usersXML = Tree.parse(usersFile)
except:
    usersRoot = Tree.Element("users")
    usersXML._setroot(usersRoot)

class User:
    username = ""
    passwordHash = ""
    disibility = None

    def __init__(self,username,passwordHash,interests: list,disability: Disabilites.Disibility):
        self.username = username
        self.passwordHash = passwordHash
        self.interests = interests
        self.disibility = disability

class Login:
    def processLogin(self,user: User):
        for user in usersXML.findall("user"):
            if (user.getchildren()[0] == user):
                if (user.getchildren()[1] == user.passwordHash):
                    return user
                else:
                    return -1
            else:
                return -2
class Register:
    def processRegister(self,newUser: User):
            usersRoot = usersXML.getroot()
            usersUserName = Tree.Element("username")
            usersUserName.text = newUser.username
            usersPasswordHash = Tree.Element("passwordHash")
            usersPasswordHash.text = newUser.passwordHash
            usersRoot.append(usersUserName)
            usersRoot.append(usersPasswordHash)
            usersXML.write("users.xml")

    def processPreferences(self,user : User, preferences: dict):
        userPreferences = Tree.Element("preferences")
        userElement = usersXML.findtext(user.username)
        for key in preferences:
            preference = Tree.Element("preference")
            preference.attrib["name"] = key
            preference.text = preferences[key]
            userPreferences.append(preference)
        userElement.append(userPreferences)

    def processDisability(self,disability: Disabilites.Disibility):
        disabilityElement = Tree.Element("disability")
        disabilityElement.attrib["name"] = disability.name
        for tag in disability.tags:
            tagElement = Tree.Element("tag")
            tagElement.text = tag
            disabilityElement.append(tagElement)






