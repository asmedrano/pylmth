from BeautifulSoup import BeautifulSoup
from pylmth.utils import *
from pylmth.spec import *

class DomObject(object):

    def __init__(self, elem_type, open_tag='', close_tag='', supportsChildren=True):
        self.elem_type = elem_type
        self.supportsChildren = supportsChildren
        self.open_tag = open_tag
        self.close_tag = close_tag
        self.attributes = {}
        self.children = []
        self._inner_text =''
        self._inner_html=''

    def attr(self, attr_name, value=None):
        """ Set or get a value from the attributes dict."""
        if attr_name not in self.attributes:
            raise ValueError("%s does not support attribute '%s'" % (self.elem_type, attr_name))
        if value is None:
            return self.attributes[attr_name]
        else:
            self.attributes[attr_name] = value

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


    def append_child(self,element):
        """ Append or Nest another element to this element """
        if not self.supportsChildren:
            raise ValueError("%s does not support children" % self.elem_type)
        self.children.append(element)

    def __build_attrs(self):
        """ Formats the attributes dict into a string """
        output = []
        for(key, value) in self.attributes.items():
            if value != None and value != '':
                output.append('%s="%s"' % (key,value))

        return ' '.join(output)

    def __get_formated_open_tag(self):
        """ Concatenates attributes into the proper spot """
        # we need to check how the opening tag is built, for example <div> vs <img
        if '>' in self.open_tag:
            tag = self.open_tag.replace('>','') # we should now have <div
            return tag + ' ' + self.__build_attrs() + '>'
        else:
            return self.open_tag + ' ' + self.__build_attrs()

    def __build_children(self):
        return "\n".join([str(child) for child in self.children])

    def __render_element(self):
        return self.__get_formated_open_tag() + self.inner_text + self.inner_html + self.__build_children() + self.close_tag

    def __str__(self):
        raw_html = BeautifulSoup(self.__render_element())
        return raw_html.prettify()


class Div(DomObject):

    def __init__(self):
        DomObject.__init__(self, 'div','<div>','</div>')




