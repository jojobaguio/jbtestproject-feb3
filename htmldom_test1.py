#create a dom instance
import pytest
from htmldom import htmldom

def test_htmldom():
	dom = htmldom.HtmlDom().createDom( """<html>
			<div id='one'><p>This is paragraph >1<strong>strong Element >1</strong></p></div>
			<div id='two'><p>This is paragraph >2<strong>strong Element >2</strong></p></div>
			<p id='three'><p>This is paragraph >3<strong>strong Element >3</strong></p></p> 
			<h4 id='four'><p>This is paragraph >4<strong>strong Element >4</strong></p></h4></html>""")
	# Getting p element from html data
	p = dom.find( "p" )
	# You can print html content using "html" method of HtmlNodeList object
	print( p.html() )
	print "\t"
	
	# Getting all elements
	all = dom.find( "*" )
	print "Getting all elements", all

	# Getting sibling elements using '+'
	sibling = dom.find( "div + div" )
	print "Getting sibling elements using '+'", sibling
	
	# Getting Descendant element
	desc = dom.find( "div p strong" )
	print "Getting Descendant element", desc

	# Getting child element using '>'
	child = dom.find( "div > p > strong" )
	print "Getting child element using '>'", child

	# Selecting elements through attributes
	elem = dom.find( "div[id=one]" )
	print "Selecting elements through attributes", elem

	#or
	elem = dom.find( "[id]" )
	print "or", elem
	
	#or
	elem = dom.find( "div[id] p" )
	print "or", elem
	
	#or
	elem = dom.find( "div#one" )
	print "or", elem
	
	#If 'one' were a class then,
	elem = dom.find( "div.one" )
	print "If 'one' were a class then", elem