from bs4 import BeautifulSoup
import urllib                                       

# test only by jojo from local branch
# test again Feb3
def test_findallhref():
	soup = BeautifulSoup(urllib.urlopen("https://winbet.cc/index.php?m=index").read(), "lxml")
	for link in soup.find_all('a'):
		print(link.get('href'))