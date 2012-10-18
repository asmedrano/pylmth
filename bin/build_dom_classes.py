# A helper for creating DomObjects from the html spec
HTML_ELEMENTS = ['html','head','title','base','link','meta','style','script','noscript','body','section','nav','article','aside','h1','h2','h3','h4','h5','h6','hgroup','header','footer','address','p','hr','pre','blockquote','ol','ul','li','dl','dt','dd','figure','figcaption','div','a','em','strong','small','s','cite','q','dfn','abbr','data','time','code','var','samp','kbd','sub','sup','i','b','u','mark','ruby','rt','rp','bdi','bdo','span','br','wbr','ins','del','img','iframe','embed','object','param','video','audio','source','track','canvas','map','area','svg','math','table','caption','colgroup','col','tbody','thead','tfoot','tr','td','th','form','fieldset','legend','label','input','button','select','datalist','optgroup','option','textarea','keygen','output','progress','meter','summary','command','menu']

template = """
class %s(DomObject):
    def __init__(self):
        DomObject.__init__(self, '%s')
"""

def main():
    for e in HTML_ELEMENTS:
        print template % (e.title(),e)


if __name__ == '__main__':
    main()
