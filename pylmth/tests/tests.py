"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from pylmth.core import *
from pylmth.utils import *
from pylmth.spec import *
from BeautifulSoup import BeautifulSoup

class TestDomObj(TestCase):

    def test_dom_attributes(self):
        d = DomObject('div')
        d.attributes = {'class':None, 'id':None}
        d.attr('class','thing')
        self.assertEqual(d.attr('class'), 'thing')

    def test_build_str_attrs(self):
        d = DomObject('div')
        d.open_tag = "<div>"
        d.close_tag="</div>"
        d.attributes = {'class':None, 'id':None}
        d.attr('class','thing')
        expected = BeautifulSoup('<div class="thing"></div>')
        self.assertEqual(str(d),expected.prettify())

    def test_inner_content(self):
        d = DomObject('div')
        d.open_tag = "<div>"
        d.close_tag="</div>"
        d.inner_text = "Hello World"
        expected = BeautifulSoup('<div>Hello World</div>')
        self.assertEqual(str(d),expected.prettify())

        # test that if we pass html to inner_text it gets stripped
        d.inner_text = "<p>Hello World <a href='asdfasdf'>google.com</a></p>"
        expected = BeautifulSoup('<div>Hello World google.com</div>')
        self.assertEqual(str(d),expected.prettify())

        # test inner_html
        d.inner_html = "<h1>Hi!</h1><img src='mypic.jpg'>"
        expected = BeautifulSoup('<div>Hello World google.com<h1>Hi!</h1><img src="mypic.jpg"></div>')
        self.assertEqual(str(d),expected.prettify())

    def test_build_str_children(self):
        d = DomObject('div')
        d.open_tag = "<div>"
        d.close_tag="</div>"
        p = DomObject('p')
        p.open_tag = "<p>"
        p.close_tag = "</p>"
        d.append_child(p)
        expected = BeautifulSoup('<div><p></p></div>')
        self.assertEqual(str(d),expected.prettify())



class TestUtils(TestCase):
    def test_strip_tags(self):
        html = "<p>Good, <b>bad</b>, and <i>ug<b>l</b><u>y</u></i></p>"
        self.assertEqual(strip_tags(html, HTML_ELEMENTS), "Good, bad, and ugly")


    if __name__ == '__main__':
        main()

