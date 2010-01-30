from zope.publisher.browser import BrowserPage
from zope.security.management import checkPermission
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from lovely.rating.interfaces import IRatable
from zojax.wizard.interfaces import ISaveable
from zojax.harvest.rss.interfaces import IHarvestedRSSItem


class ItemView(BrowserPage):

    template = ViewPageTemplateFile("item.pt")

    def __call__(self):

        item = IHarvestedRSSItem(self.context)
        self.title = item.title
        self.description = item.summary
        self.url = item.url
        self.author = item.author
        self.source = item.sourceTitle
        self.feedTitle = u""

        self.ratable = IRatable.providedBy(self.context)
        self.saveable = ISaveable.providedBy(self.context)
        self.canSave = self.saveable and checkPermission('gadoz.portfolio.Save', self.context)
        self.showActions = self.ratable or self.saveable
        
        return self.template()
