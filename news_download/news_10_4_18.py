import csv
import feedparser
from newspaper import Article


output = open('news_21_3.csv', 'a')
writer = csv.writer(output)
writer.writerow(["title","link","published","full-text","summary","keywords"])

"""
feed_url_list=["http://timesofindia.indiatimes.com/rssfeeds/3908999.cms",
			   "http://infotech.indiatimes.com/rssfeedsdefault.cms",
			   "http://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms",
			   "http://timesofindia.indiatimes.com/rssfeeds/5880659.cms",
			   "https://www.hindustantimes.com/rss/tech/rssfeed.xml",
			   "https://www.hindustantimes.com/rss/health-fitness/rssfeed.xml",
			   "http://www.newindianexpress.com/Life-Style/Health/rssfeed/?id=213&getXmlFeed=true",
			   "http://www.newindianexpress.com/Life-Style/Tech/rssfeed/?id=212&getXmlFeed=true",
			   "http://syndication.indianexpress.com/rss/698/science---technology.xml",
			   "http://syndication.indianexpress.com/rss/697/health.xml"] 
			   """
			   
newlist=["http://timesofindia.indiatimes.com/rssfeeds/2647163.cms","http://timesofindia.indiatimes.com/rssfeeds/913168846.cms",
"http://timesofindia.indiatimes.com/rssfeeds/1081479906.cms","https://www.hindustantimes.com/rss/travel/rssfeed.xml",
"https://www.hindustantimes.com/rss/education/rssfeed.xml","https://www.hindustantimes.com/rss/books/rssfeed.xml",
"https://www.hindustantimes.com/rss/art-culture/rssfeed.xml","https://www.hindustantimes.com/rss/fashion-trends/rssfeed.xml",
"http://www.newindianexpress.com/Life-Style/Travel/rssfeed/?id=214&getXmlFeed=true"]

new=[
"http://www.newindianexpress.com/Life-Style/Food/rssfeed/?id=215&getXmlFeed=true",
"http://www.newindianexpress.com/Life-Style/Books/rssfeed/?id=216&getXmlFeed=true"]



#feed_url_list=["http://feeds.feedburner.com/ndtvcooks-latest","http://feeds.feedburner.com/gadgets360-latest"]

for k in new:
	feed = feedparser.parse(k)
	for news in feed['items']:
		toi_url = news["link"]
		toi_article = Article(toi_url, language="en") # en for English
		l=[]
		toi_article.download()
		toi_article.parse()
		toi_article.nlp()
		l.append(toi_article.title)
		l.append(news["link"])
		l.append(news["published"])
		l.append(toi_article.text)
		l.append(toi_article.summary)
		l.append(toi_article.keywords)
		writer.writerow(l)
