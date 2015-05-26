import urllib2
import json
import re

startNum = 1
jsonOutput = None

def makeRequest ():
	url = "http://api.npr.org/query?id=93559255&apiKey=MDA2OTI5NDExMDEyOTY3ODIwNjBlYTFhOA001" + "&startNum=" + str(startNum) + "&output=JSON"

	req = urllib2.Request(url)

	response = urllib2.urlopen(req)

	return json.loads(response.read())

regexBlacklist = [(r"^This coming.+fresh air\.$"),(r"Find us:.+(Tumblr|Spotify|Flickr|Facebook) ?\.?"),(r"Download.+([sS]ubscribe|[aA]pp|here) ?\.?"),(r"To download.+above\."),(r"Note:.+(2011|2010|radio|year|2009|blurred) ?\."),(r"\[Copyright.+NPR\]"),(r"Subscribe.|.+(podcast|iTunes) ?\.?"),(r"Listen.+(soundtrack|borders) ?\.?"),(r"For more.+(Suboxone|Magazine|column)?\.?"),(r"Check out.+coverage\.?"),(r"We learned.+This?\.?"),(r"Update.+2011?\.?")]

musicArray = []
jsonOutput = makeRequest()

while jsonOutput["list"].get("story", "") != "":
	for blogEntry in jsonOutput["list"]["story"]:
		for listItem in blogEntry["text"]["paragraph"]:
			if "Music:" in listItem.get("$text", ""):

				episodeTitle = blogEntry["title"]["$text"]
				musicData = listItem["$text"]
 
				for indRegex in regexBlacklist:
					#musicData = musicData.replace(indString, "") #use this if not using regex, plug strings back into regexBlackList(formerly known as stringArray) indString = indRegex
					musicData = re.sub(indRegex,"",musicData)

				titleAndMusic = ({"episodeTitle": episodeTitle, "musicData": musicData})
					
				musicArray.append(titleAndMusic)
				#print blogEntry["title"]["$text"]
				#print listItem["$text"]
				print titleAndMusic

	startNum = startNum + 20
	jsonOutput = makeRequest()

#f = open("musicRows.json","w")
#json.dump(musicArray, f)
#f.close()

f = open("/Users/kate/desktop/github/website/projects/planet/myJsonData.js","w")
jsOutput = "var JsonData = " + json.dumps(musicArray)
f.write(jsOutput);
f.close()


#Strings targeted with regex:

#"Find us: Twitter/ Facebook/ Spotify/ Tumblr.",
#"Find us:Twitter/ Facebook/ Spotify/ Tumblr.",
#"Find us: Twitter / Facebook/ Spotify/ Tumblr.",
#"Find us: Twitter/Facebook/ Spotify/ Tumblr",
#"Find us: Twitter/ Facebook/Spotify/ Tumblr.",
#"Find us: Twitter/Facebook/Spotify/Tumblr.",
#"Find us: Twitter/ Facebook/ Spotify/ Tumblr",
#"Find us: Twitter / Facebook / Spotify / Tumblr.",
#"Find us: Twitter/ Facebook/ Spotify/Tumblr",
#"Find us:Twitter/Facebook/ Spotify/ Tumblr.",
#"Find us: Twitter/Facebook/Tumblr .",
#"Find us: Twitter/Facebook/ Spotify.",
#"Find us: Twitter/ Facebook/ Spotify.",
#"Find us: Twitter/ Facebook/Spotify",
#"Find us: Twitter/ Facebook/ Flickr.",
#"Find us:Twitter/ Facebook.",
#"Find us: Twitter/ Facebook.",
#"Find us:Twitter/ Facebook",
#"Download the PlanetMoney iPhone App.",
#"Subscribe to the podcast.",
#"Subscribe to the podcast in iTunes.",
#"Subscribe to the podcast in iTunes.",
#"Download the podcast; or subscribe.",
#"Download the podcast, or subscribe. ",
#"To download the podcast, click on the arrow icon in the podcast player above.",
#"Download the Planet Money iPhone App.",
#"This coming Monday (May 25) will be my six month anniversary of unemployment. Since that period, my life has become a cliche. I'm a jazz saxophonist/composer in New York with a master's degree from an Ivy League music school (New England Conservatory of Music), and I've got the student loan debt to prove it. Three years ago, after filling in as a college professor in Fairbanks, Alaska, I moved back to NYC (lived here twice before) in hopes of becoming a member of the community of musicians that I admire so much. And around that time, I made peace with the idea that I would have to work in an office in order to facilitate my music career goals. I know a lot of artistic people look down upon office work as a necessary evil, but compared to playing weddings and cruise ship gigs, sitting in an office and punching formulas into Excel is a breath of fresh air.",
#"[Copyright 2015 NPR]",
#"Note: This podcast originally aired in January, 2011.",
#"Note: This podcast was originally published in December, 2010.",
#"Note: Today's podcast originally aired in 2010.",
#"Note: These stories initially aired on the radio.",
#"Note: Our interview with Thomas Petterfy originally posted last year.",
#"Note: This podcast originally aired in December, 2009.",
#"Note: Some information in the photo was intentionally blurred.",
#"For more, see this paper on the history of Suboxone.",
#"For more, see the article Whitewood under Siege in Cabinet Magazine.",
#"For more, see this New York Times Magazine column.",
#"Listen to our Elko soundtrack.",
#"Listen to the rest of our series on European borders.",
#"Download the Planet MoneyiPhone App.",
#"Download the podcast here; subscribe here. Follow our Twitter feed here.",
#"Download the Planet Money iPhone app .",
#"Download the podcast, or Subscribe.",
#"Check out the rest of our Haiti coverage.",
#"We learned of Peterffy's story from the book Automate This.",
#"Update: Our interview with Cynder Niemla was recorded on Dec. 2, 2011."
