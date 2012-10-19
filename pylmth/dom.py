from pylmth.core import DomObject


class Html(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'html', prettify)


class Head(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'head', prettify)


class Title(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'title', prettify)


class Base(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'base', prettify)


class Link(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'link', prettify)


class Meta(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'meta', prettify)


class Style(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'style', prettify)


class Script(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'script', prettify)


class Noscript(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'noscript', prettify)


class Body(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'body', prettify)


class Section(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'section', prettify)


class Nav(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'nav', prettify)


class Article(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'article', prettify)


class Aside(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'aside', prettify)


class H1(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'h1', prettify)


class H2(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'h2', prettify)


class H3(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'h3', prettify)


class H4(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'h4', prettify)


class H5(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'h5', prettify)


class H6(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'h6', prettify)


class Hgroup(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'hgroup', prettify)


class Header(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'header', prettify)


class Footer(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'footer', prettify)


class Address(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'address', prettify)


class P(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'p', prettify)


class Hr(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'hr', prettify)


class Pre(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'pre', prettify)


class Blockquote(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'blockquote', prettify)


class Ol(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'ol', prettify)

    def add_li(self,inner_text='',inner_html='',id='',className=''):
        li = Li()
        li.inner_text=inner_text
        li.inner_html=inner_html
        li.attr.id=id
        li.attr.className=className
        self.append_child(li)
        return li

class Ul(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'ul', prettify)

    def add_li(self,inner_text='',inner_html='',id='',className=''):
        li = Li()
        li.inner_text=inner_text
        li.inner_html=inner_html
        li.attr.id=id
        li.attr.className=className
        self.append_child(li)
        return li

class Li(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'li', prettify)


class Dl(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'dl', prettify)


class Dt(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'dt', prettify)


class Dd(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'dd', prettify)


class Figure(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'figure', prettify)


class Figcaption(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'figcaption', prettify)


class Div(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'div', prettify)


class A(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'a',prettify, unique_attrs=('href', 'target','rel'))


class Em(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'em', prettify)


class Strong(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'strong', prettify)


class Small(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'small', prettify)


class S(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 's', prettify)


class Cite(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'cite', prettify)


class Q(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'q', prettify)


class Dfn(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'dfn', prettify)


class Abbr(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'abbr', prettify)


class Data(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'data', prettify)


class Time(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'time', prettify)


class Code(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'code', prettify)


class Var(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'var', prettify)


class Samp(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'samp', prettify)


class Kbd(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'kbd', prettify)


class Sub(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'sub', prettify)


class Sup(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'sup', prettify)


class I(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'i', prettify)


class B(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'b', prettify)


class U(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'u', prettify)


class Mark(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'mark', prettify)


class Ruby(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'ruby', prettify)


class Rt(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'rt', prettify)


class Rp(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'rp', prettify)


class Bdi(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'bdi', prettify)

class Bdo(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'bdo', prettify)


class Span(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'span', prettify)


class Br(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'br', prettify)


class Wbr(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'wbr', prettify)


class Ins(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'ins')


class Del(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'del')


class Img(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'img',prettify, unique_attrs=('src', 'width', 'height'))

class Iframe(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'iframe', prettify)


class Embed(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'embed', prettify)


class Object(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'object', prettify)


class Param(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'param', prettify)


class Video(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'video', prettify)


class Audio(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'audio', prettify)


class Source(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'source', prettify)


class Track(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'track', prettify)


class Canvas(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'canvas', prettify)


class Map(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'map', prettify)


class Area(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'area', prettify)


class Svg(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'svg', prettify)


class Math(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'math', prettify)


class Table(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'table', prettify,('border',))

    def add_header(self, inner_text='', inner_html='', id='', className=''):
        thead = Thead()
        thead.inner_text = inner_text
        thead.inner_html = inner_html
        thead.attr.id = id
        thead.attr.className = className
        self.append_child(thead)
        return thead

    def add_body(self, inner_html='', id='', className=''):
        tbody = Tbody()
        tbody.inner_html = inner_html
        tbody.attr.id = id
        tbody.attr.className = className
        self.append_child(tbody)
        return tbody

    def add_row(self, inner_html='', id='', className=''):
        tr = Tr()
        tr.inner_html = inner_html
        tr.attr.id = id
        tr.attr.className = className
        self.append_child(tr)
        return tr


class Caption(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'caption', prettify)


class Colgroup(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'colgroup', prettify)


class Col(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'col', prettify)


class Tbody(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'tbody', prettify)

    def add_row(self, inner_html='', id='', className=''):
        tr = Tr()
        tr.inner_html = inner_html
        tr.attr.id = id
        tr.attr.className = className
        self.append_child(tr)
        return tr


class Thead(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'thead', prettify)

    def add_row(self, inner_html='', id='', className=''):
        tr = Tr()
        tr.inner_html = inner_html
        tr.attr.id = id
        tr.attr.className = className
        self.append_child(tr)
        return tr


class Tfoot(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'tfoot', prettify)


class Tr(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'tr', prettify)

    def add_col(self, inner_text='', inner_html='', id='', className='', colspan=''):
        if self.parent.elem_type =='thead':
            col = Th()
        else:
            col = Td()
        col.inner_text = inner_text
        col.inner_html = inner_html
        col.attr.colspan=colspan
        col.attr.id = id
        col.attr.className = className
        self.append_child(col)
        return col

class Td(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'td', prettify, ('colspan','rowspan','headers', 'rel'))


class Th(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'th', prettify, ('colspan','rowspan','headers', 'scope'))


class Form(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'form', prettify)


class Fieldset(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'fieldset', prettify)


class Legend(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'legend', prettify)


class Label(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'label', prettify)


class Input(DomObject):
    def __init__(self, prettify=True):
        unique_attrs = (
                'value',
                'type',
                'size',
                'src',
                'step',
                'required',
                'readonly',
                'placeholder',
                'pattern',
                'name',
                'mulitiple',
                'min',
                'maxlength',
                'max',
                'list',
                'height',
                'width',
                'formtarget',
                'formnovalidate',
                'formmethod',
                'formenctype',
                'formaction',
                'form',
                'disabled',
                'checked',
                'autofocus',
                'alt',
                'align',
                'accept'

                )
        DomObject.__init__(self, 'input', prettify, unique_attrs)


class Button(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'button', prettify)


class Select(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'select', prettify)


class Datalist(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'datalist', prettify)


class Optgroup(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'optgroup', prettify)


class Option(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'option', prettify)


class Textarea(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'textarea', prettify)


class Keygen(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'keygen', prettify)


class Output(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'output', prettify)


class Progress(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'progress', prettify)


class Meter(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'meter', prettify)


class Summary(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'summary', prettify)


class Command(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'command', prettify)


class Menu(DomObject):
    def __init__(self, prettify=True):
        DomObject.__init__(self, 'menu', prettify)

