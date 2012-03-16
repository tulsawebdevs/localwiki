"""
We prefer lxml where available, but we also run without it.  This
lets us import fragments_fromstring and etree in a generic fashion,
plugging up holes where they exist.
"""

#try:
#from lxml import etree
#    from lxml.html import fragments_fromstring
#except ImportError:
import xml.etree.cElementTree as etree
#import xml.etree.cElementTree as etree
import html5lib


try:
    etree.tostring(etree.Element('div'), method='html')
except TypeError:
    # We're on python 2.6 and ElementTree doesn't have method types.  So
    # we'll use our packaged ElementTree.
    import ElementTree as etree


html5_parser = html5lib.HTMLParser(
    tree=html5lib.treebuilders.getTreeBuilder("etree", etree),
    namespaceHTMLElements=False)
fragments_fromstring = html5_parser.parseFragment
