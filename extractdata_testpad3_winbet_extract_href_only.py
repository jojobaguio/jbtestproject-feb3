# encoding=utf8  
import sys 
from bs4 import BeautifulSoup
import requests
import pytest
import time
import unittest
#import md5
import codecs
reload(sys)  
sys.setdefaultencoding('utf8')
import urllib2
import re

def test_getwebdata():
	# site tested >> https://www.bct6686.co , https://winbet.cc/index.php?m=index , https://www.8848bo.com	
	html = '''
	<a href="/index.php?file=danbao.html">Facebook</a>,  
	<a href="?Company=XOM">Exxon</a>,  
	<a href="/index.php?c=clist&a=url&id=35">Technology</a>,  
	<a href="/index.php?c=clist&a=url&id=10">Oil & Gas</a>] 
	<a href="?Organization=3">Oil & Gas</a>]
	'''
	html2 = urllib2.urlopen("https://winbet.cc/index.php?m=index").read()
	print "\t"
	soup = BeautifulSoup(html2, "lxml")
	count = 0
	print "========================================================================="
	print "EXTRACTED href LINKS are the following:"
	for a in soup.find_all('a', href=True):
		valhref = a['href'] 
		#print valhref
		includestr = ['/index.php?']
		if any(x in valhref for x in includestr):
			count = count + 1
			#IMPORTANT: the strip here will removed all leading spaces from the link that will be found....
			url2 = valhref.strip()
			r2  = requests.get("https://winbet.cc" +url2)
			result = str("https://winbet.cc" +url2)
			with open('./datasource/storelinks_hrefonly_winbet.csv', 'a') as the_file1:
				the_file1.write(result + '\n')
				data2 = r2.text
				soup2 = BeautifulSoup(data2, "lxml")
				print count,"'href' data found >>>", "https://winbet.cc"+url2
				countstr = str(count)
				res = str(result)
				m = re.search("(file=.*)", res)
				if m:
					getsrch = m.group(1)
					with open("./datasource/hreflinks/"+getsrch+".html", 'a') as the_file:
						the_file.write(soup2.encode('ISO-8859-1') + '\n')
				m = re.search("(c=.*)", res)
				if m:
					getsrch = m.group(1)
					with open("./datasource/hreflinks/"+getsrch+".html", 'a') as the_file:
						the_file.write(soup2.encode('ISO-8859-1') + '\n')			