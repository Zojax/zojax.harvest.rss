from zope import interface, schema
from zojax.richtext.field import RichText
from zojax.content.models.container.interfaces import _


class IHarvestedRSSModel(interface.Interface):
    """ harvested rss view model """

    pageSize = schema.Int(
        title = _(u'Page size'),
        description = _(u'Number of items per page.'),
        default = 20,
        required = False)

    text = RichText(
        title = _(u'Text'),
        description = _(u'Folder preview text.'),
        required = False)


class IHarvestedRSSView(interface.Interface):
    """ harvested rss view """