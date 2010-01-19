from zope import interface, schema
from z3ext.content.space.interfaces import IWorkspace, IWorkspaceFactory
from z3ext.content.type.interfaces import IItem
from zojax.harvest.rss import _
from zojax.harvest.rss.fields import FeedsField


class IHarvestRSSProduct(interface.Interface):
    """ product """


class IHarvestedRSSWorkspace(IWorkspace):
    """ harvested content workspace """
    
    feeds = FeedsField(title=_(u"Feeds"),
                       value_type = schema.TextLine(title=_(u"Feed")),
                       required=True)

    def harvest():
        """ harvest rss """
    

class IHarvestedRSSWorkspaceFactory(IWorkspaceFactory):
    """ factory """


class IHarvestedRSSItem(IItem):

    id = schema.TextLine(
         title=_(u'ID'),
         required=True)

    url = schema.URI(
         title=_(u'URL'),
         required=True)
    
    feedURL = schema.URI(
         title=_(u'URL'),
         required=True)
    
    summary = schema.Text(
         title=_(u'Summary'),
         required=False)
    
    author = schema.TextLine(
         title=_(u'Author'),
         required=False)
    
    published = schema.Datetime(
         title=_(u'Published'),
         required=False)


class IHarvestedRSSItemType(interface.Interface):
    """ harvested rss item content type marker interface """


