from xml.dom import minidom
import requests
print("###########################")
print("# Name = Mac Searcher")
print("# Version = 0.1")
print("# Searcher = Yandex")
print("###########################")
Mac = input("# Input MAC: ").upper().rstrip(":")
Text = requests.get("http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks={}:-65&app=ymetro".format(Mac)).text
print("###########################")
Parser = minidom.parseString(Text)
Parser.normalize()
Coordinates = Parser.getElementsByTagName("coordinates")[0]
latitude = Coordinates.getAttribute("latitude")
longitude = Coordinates.getAttribute("longitude")
print("Latitude = " + str(latitude))
print("Longitude = " + str(longitude))
print("###########################")