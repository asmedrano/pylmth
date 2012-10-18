from BeautifulSoup import BeautifulSoup, NavigableString

def strip_tags(html, invalid_tags):
    soup = BeautifulSoup(html)

    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""

            for c in tag.contents:
                if not isinstance(c, NavigableString):
                    c = strip_tags(unicode(c), invalid_tags)
                s += unicode(c)

            tag.replaceWith(s)

    return soup.renderContents()


class ElementAttributes(object):
    """
    An object to hold data. Motivated by a desire for a mutable namedtuple with
    default values. To use, subclass, and define __slots__.

    The default default value is None. To set a default value other than None,
    set the `default_value` class variable.

    Example:
        class Jello(DataObject):
            default_value = 'no data'
            __slots__ = (
                'request_date',
                'source_id',
                'year',
                'group_id',
                'color',
                # ...
            )

    http://stackoverflow.com/a/472024/101911 says __slots__ should not be used
    for the purposes of control freaks, but I didn't know the better way.
    """

    default_value = None

    def __init__(self, slots, *args, **kwargs):
        self.__slots__ = slots
        for att in self.__slots__:
            setattr(self, att, self.default_value)
        # Set attributes passed in as arguments
        self.set(*args, **kwargs)

    def set(self, *args, **kwargs):
        for k, v in zip(self.__slots__, args):
            setattr(self, k, v)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def asdict(self):
        return dict(
            (att, getattr(self, att)) for att in self.__slots__)

    def astuple(self):
        return tuple(getattr(self, att) for att in self.__slots__)

# This is not necessary. If __slots__ is defined in DataObject and the subclass,
# any attribute not in __slots__ will automatically raise an AttributeError.
#     def __setattr__(self, name, value):
#         if name not in self.__slots__:
#             raise AttributeError("%s is not a valid attribute in %s" % (
#                     name, self.__class__.__name__))
#         super(DataObject, self).__setattr__(name, value)

    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join('{}={}'.format(
                    att, repr(getattr(self, att))) for att in self.__slots__))

