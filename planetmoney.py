import urllib2
import json

startNum = 1
jsonOutput = None

def makeRequest ():
	url = "http://api.npr.org/query?id=93559255&apiKey=MDA2OTI5NDExMDEyOTY3ODIwNjBlYTFhOA001" + "&startNum=" + str(startNum) + "&output=JSON"

	req = urllib2.Request(url)

	response = urllib2.urlopen(req)

	return json.loads(response.read())


jsonOutput = makeRequest()

while jsonOutput["list"].get("story", "") != "":
	for blogEntry in jsonOutput["list"]["story"]:
		for listItem in blogEntry["text"]["paragraph"]:
			if "Music" in listItem.get("$text", ""):
				musicData = listItem["$text"]

				f = open("musicRows.json", "/n", "a")
				json.dump(musicData, f)
				f.close()

				print listItem["$text"]

	
	startNum = startNum + 20
	jsonOutput = makeRequest()



