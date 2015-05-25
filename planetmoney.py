import urllib2
import json

startNum = 1
jsonOutput = None

def makeRequest ():
	url = "http://api.npr.org/query?id=93559255&apiKey=MDA2OTI5NDExMDEyOTY3ODIwNjBlYTFhOA001" + "&startNum=" + str(startNum) + "&output=JSON"

	req = urllib2.Request(url)

	response = urllib2.urlopen(req)

	return json.loads(response.read())

stringArray = ["Find us: Twitter/ Facebook/ Spotify/ Tumblr.","Find us:Twitter/ Facebook/ Spotify/ Tumblr.", "Find us: Twitter / Facebook/ Spotify/ Tumblr.","Find us: Twitter/Facebook/ Spotify/ Tumblr","Find us: Twitter/ Facebook/Spotify/ Tumblr.","Find us: Twitter/Facebook/Spotify/Tumblr.","Find us: Twitter/ Facebook/ Spotify/ Tumblr","Find us: Twitter / Facebook / Spotify / Tumblr.","Find us: Twitter/ Facebook/ Spotify/Tumblr","Find us:Twitter/Facebook/ Spotify/ Tumblr.","Find us: Twitter/Facebook/Tumblr .","Find us: Twitter/Facebook/ Spotify.","Find us: Twitter/ Facebook/ Spotify.","Find us: Twitter/ Facebook/Spotify","Find us: Twitter/ Facebook/ Flickr.","Find us: Twitter/ Facebook.","Find us:Twitter/ Facebook.","Find us:Twitter/ Facebook","Download the PlanetMoney iPhone App.","Subscribe to the podcast.","Download the podcast; or subscribe.","Download the podcast, or subscribe. ","To download the podcast, click on the arrow icon in the podcast player above.","Follow our Twitter feed.","Join our Facebook group.","Download the Planet Money iPhone App.","This coming Monday (May 25) will be my six month anniversary of unemployment. Since that period, my life has become a cliche. I'm a jazz saxophonist/composer in New York with a master's degree from an Ivy League music school (New England Conservatory of Music), and I've got the student loan debt to prove it. Three years ago, after filling in as a college professor in Fairbanks, Alaska, I moved back to NYC (lived here twice before) in hopes of becoming a member of the community of musicians that I admire so much. And around that time, I made peace with the idea that I would have to work in an office in order to facilitate my music career goals. I know a lot of artistic people look down upon office work as a necessary evil, but compared to playing weddings and cruise ship gigs, sitting in an office and punching formulas into Excel is a breath of fresh air.","Check out a graphic that tracks the carpenters' toxic asset.","[Copyright 2015 NPR]","Note: This podcast originally aired in January, 2011.","Note: This podcast was originally published in December, 2010.","Note: Today's podcast originally aired in 2010.","Note: These stories initially aired on the radio.","Music is an export, just like anything else. And, as with other exports, businesses in lots of other countries are fighting for their share of the global market. They want people all around to world to be listening to their music. And they're figuring out how to make it happen.","Yes, there's a spoiler in this post. But the movie came out 30 years ago. Deal with it.","For more, see this paper on the history of Suboxone.","For more, see our story Why More People Are Renting Tires. And see the paper we mention on the show,  U.S. Tire Tariffs: Saving Few Jobs at High Cost.","In our Friday podcast, guest host Frannie Kelly of NPR Music compared Jonathan Coulton to a Snuggie, arguing that his success was a fluky thing that would be hard for other musicians to replicate.","Listen to our other stories from Jamaica.", "That's more than twice the cost of the previous record holder, Shrek The Musical, according to Catherine Rampell over at the NYT's Economix blog.","Subscribe to the podcast in iTunes.","Download the Planet MoneyiPhone App.","Download the podcast here; subscribe here. Follow our Twitter feed here."," (sound art?)","\"http://www.amazon.com/Sound-Silver-LCD-Soundsystem/dp/B000M3452Y\">"]

musicArray = []
jsonOutput = makeRequest()

while jsonOutput["list"].get("story", "") != "":
	for blogEntry in jsonOutput["list"]["story"]:
		for listItem in blogEntry["text"]["paragraph"]:
			if "Music" in listItem.get("$text", ""):

				episodeTitle = blogEntry["title"]["$text"]
				musicData = listItem["$text"]
 
				for indString in stringArray:
					musicData = musicData.replace(indString, "")

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

f = open("myJsonData.js","w")
jsOutput = "var JsonData = " + json.dumps(musicArray)
f.write(jsOutput);
f.close()
