from zope import interface
from zope.schema.fieldproperty import FieldProperty
from zojax.content.type.item import Item
from zojax.harvest.rss.interfaces import IHarvestedRSSItem
from zojax.content.type.interfaces import ITitleBasedName


class HarvestedRSSItem(Item):
    interface.implements(IHarvestedRSSItem, ITitleBasedName)
    
    id = FieldProperty(IHarvestedRSSItem['id'])
    feedURL = FieldProperty(IHarvestedRSSItem['feedURL'])
    url = FieldProperty(IHarvestedRSSItem['url'])
    summary = FieldProperty(IHarvestedRSSItem['summary'])
    author = FieldProperty(IHarvestedRSSItem['author'])
    published = FieldProperty(IHarvestedRSSItem['published'])
