from zope import interface

from zojax.batching.batch import Batch
from zope.app import zapi
from interfaces import IHarvestedRSSView


class HarvestedRSSView(object):
    interface.implements(IHarvestedRSSView)

    def __init__(self, context, request):
        self.model = context
        super(HarvestedRSSView, self).__init__(context.__parent__, request)

    def update(self):
        model = self.model
        
        self.contents = Batch(list(self.context.values()), size=model.pageSize, request=self.request)
        self.came_from = zapi.absoluteURL(self, self.request)
        qs = self.request.get('QUERY_STRING')
        if qs:
            self.came_from = '%s?%s' % (self.came_from, qs)
