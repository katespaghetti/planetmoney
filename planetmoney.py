import urllib2
import json

startNum = 1
jsonOutput = None

def makeRequest ():
	url = "http://api.npr.org/query?id=93559255&apiKey=MDA2OTI5NDExMDEyOTY3ODIwNjBlYTFhOA001" + "&startNum=" + str(startNum) + "&output=JSON"

	req = urllib2.Request(url)

	response = urllib2.urlopen(req)

	return json.loads(response.read())

musicArray = []
jsonOutput = makeRequest()

while jsonOutput["list"].get("story", "") != "":
	for blogEntry in jsonOutput["list"]["story"]:
		for listItem in blogEntry["text"]["paragraph"]:
			if "Music" in listItem.get("$text", ""):

				episodeTitle = blogEntry["title"]["$text"]
				musicData = listItem["$text"]

				titleAndMusic = ({"episodeTitle": episodeTitle, "musicData": musicData})
				
				musicArray.append(titleAndMusic)
				#print blogEntry["title"]["$text"]
				#print listItem["$text"]
				print titleAndMusic

	startNum = startNum + 20
	jsonOutput = makeRequest()

f = open("musicRows.json","w")
json.dump(musicArray, f)
f.close()


