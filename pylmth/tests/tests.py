"""
Run tests like so:
    python -m unittest discover
Make sure its from the main module directory!
SEE: http://docs.python.org/library/unittest.html#test-discovery
"""
from unittest import TestCase, main
from pylmth.core import *
from pylmth.dom import *
from pylmth.utils import *
from pylmth.spec import *
from bs4 import BeautifulSoup

class TestDomObj(TestCase):

    def test_dom_elem_valid(self):
        self.assertRaises(ValueError, DomObject, 'bean')

    def test_dom_elem_tags(self):
        reg = DomObject('div', prettify=False)
        void = DomObject('img', prettify=False)
        self.assertEqual(str(reg),'<div></div>')
        self.assertEqual(str(void),'<img/>')

    def test_dom_attributes(self):
        d = DomObject('div')
        d.attr.className = 'thing'
        self.assertEqual(d.attr.className, 'thing')

    def test_dom_add_unique_attrs(self):
        d = DomObject('div', prettify=False)
        d.add_attr('my-attr')
        d.attr.my_attr = "test"

        self.assertEqual(str(d), '<div my-attr="test"></div>')


    def test_build_str_attrs(self):
        d = DomObject('div')
        d.attr.className = "thing"
        expected = BeautifulSoup('<div class="thing"></div>')
        self.assertEqual(str(d),expected.prettify())

    def test_inner_content(self):
        d = DomObject('div')
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
        p = DomObject('p')
        d.append_child(p)
        expected = BeautifulSoup('<div><p></p></div>')
        self.assertEqual(str(d),expected.prettify())

class TestDomAbstractions(TestCase):

    def test_general(self):
        div = Div()
        div.attr.id = "hi"
        h1 = H1()
        h1.inner_text = "Hello World!"
        img = Img()
        img.attr.id = "theimg"
        img.attr.src = "myimg.jpg"
        div.append_child(h1, img)
        expected = BeautifulSoup('<div id="hi"><h1>Hello World!</h1><img id="theimg" src="myimg.jpg" /></div>')
        self.assertEqual(str(div),expected.prettify())

    def test_elems_with_helpers(self):
        """Most elements just have global attributes and such but these have helper methods built in"""
        #ul
        ul = Ul(False)
        for i in ['hi', 'there']:
            ul.add_li(inner_text=i)
        self.assertEqual(str(ul),"<ul><li>hi</li><li>there</li></ul>")

        ol = Ol(False)
        for i in ['hi', 'there']:
            ol.add_li(inner_text=i)
        self.assertEqual(str(ol),"<ol><li>hi</li><li>there</li></ol>")

        tbl = Table(False)
        thead = tbl.add_header()
        row = thead.add_row()
        row.add_col(inner_text='Beans', colspan='2')
        row.add_col(inner_text='Rice')
        tbody = tbl.add_body()
        tr = tbody.add_row()
        tr.add_col(inner_text='pinto', className='foo')
        tr.add_col(inner_text='jasmine', className='foo')
        self.assertEqual(str(tbl), '<table><thead><tr><th colspan="2">Beans</th><th>Rice</th></tr></thead><tbody><tr><td class="foo">pinto</td><td class="foo">jasmine</td></tr></tbody></table>')


class TestUtils(TestCase):
    def test_strip_tags(self):
        html = "<p>Good, <b>bad</b>, and <i>ug<b>l</b><u>y</u></i></p>"
        self.assertEqual(strip_tags(html, HTML_ELEMENTS), "Good, bad, and ugly")

    if __name__ == '__main__':
        main()
