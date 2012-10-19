from collections import namedtuple
from BeautifulSoup import BeautifulSoup
from pylmth.utils import *
from pylmth.spec import *

class DomObject(object):

    def __init__(self, elem_type, prettify=True, unique_attrs=()):
        if elem_type not in HTML_ELEMENTS:
            raise ValueError("%s element not supported" % elem_type)

        # set opening and closing tags based on spec
        if elem_type in VOID_ELEMENTS:
            self.open_tag = '<%s' % elem_type
            self.close_tag = '>'
            self.supports_children = False
        else:
            self.open_tag = '<%s>' % elem_type
            self.close_tag = '</%s>' % elem_type
            self.supports_children = True

        self.elem_type = elem_type
        self._prettify = prettify
        self.attr = ElementAttributes(GLOBAL_ATTRIBUTES + unique_attrs)
        self.children = []
        self._inner_text =''
        self._inner_html=''
        self.parent = None # a reference to the parent element of this element

    @property
    def inner_html(self):
        return self._inner_html

    @inner_html.setter
    def inner_html(self, html):
        self._inner_html = html

    @property
    def inner_text(self):
        return self._inner_text

    @inner_text.setter
    def inner_text(self, text):
        """ inner_text converts any strips any html in param:text"""
        self._inner_text = strip_tags(text, HTML_ELEMENTS)

    @property
    def prettify(self):
        return self._prettify

    @prettify.setter
    def prettify(self, value):
        self._prettify = value
        # we have to update all the children
        for child in self.children:
            child.prettify = self._prettify

    def append_child(self, *args):
        """ Append or Nest another element or elements to this element """
        if not self.supports_children:
            raise ValueError("%s does not support children" % self.elem_type)
        for arg in args:
            # set this childs "prettify" to the same as the parent
            arg.prettify = self.prettify
            arg.parent = self
            self.children.append(arg)

    def __build_attrs(self):
        """ Formats the attributes dict into a string """
        output = []
        for(key, value) in self.attr.asdict().items():
            if value != None and value != '':
                output.append('%s="%s"' % (key,value))

        outstr =  ' '.join(output)
        outstr = outstr.replace('className', 'class') #hack!
        return outstr

    def __get_formated_open_tag(self):
        """ Concatenates attributes into the proper spot """
        # we need to check how the opening tag is built, for example <div> vs <img
        if '>' in self.open_tag:
            tag = self.open_tag.replace('>','') # we should now have <div
            return tag + ' ' + self.__build_attrs() + '>'
        else:
            return self.open_tag + ' ' + self.__build_attrs()

    def __build_children(self):
        return "".join([str(child) for child in self.children])

    def __render_element(self):
        return self.__get_formated_open_tag() + self.inner_text + self.inner_html + self.__build_children() + self.close_tag

    def __str__(self):
        raw_html = BeautifulSoup(self.__render_element())
        if self.prettify:
            return raw_html.prettify()
        else:
            return raw_html.renderContents()
