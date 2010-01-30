from zope.cachedescriptors.property import Lazy
from zope.publisher.browser import BrowserView
from z3c.batching.batch import first_neighbours_last
from zope.app import zapi
from urllib import urlencode


class Navigation(BrowserView):
    
    @Lazy
    def batch(self):
        return self.context.contents
        
    @Lazy
    def nextBatchStart(self):
        if self.batch.number == self.batch.total: # Last batch
            return None        
        return (self.batch.index + 1) * self.batch.size
    
    @Lazy
    def prevBatchStart(self):
        if self.batch.index == 0: # First batch
            return None
        return (self.batch.index - 1) * self.batch.size
    
    @Lazy
    def batches(self):
        return first_neighbours_last(self.batch.batches, self.batch.index, 3, 3)

    def createBatchLink(self, batchStart):
        listing = self.context
        url = zapi.absoluteURL(listing, self.request).replace("%2F","/")
        url += "?"
        url += urlencode({'bstart':batchStart})
        return url
    
    def isAvailable(self):
        return True
        