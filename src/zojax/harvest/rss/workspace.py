from zope import interface, component, event
from zope.app.component.hooks import setSite
from zope.schema.fieldproperty import FieldProperty

from ZODB.interfaces import IDatabase

from scheduler.interfaces import ITask
from scheduler.loop import LoopTask

from zojax.catalog.interfaces import ICatalogConfiglet
from zojax.content.space.interfaces import ISpace
from zojax.content.space.workspace import WorkspaceFactory
from zojax.content.type.container import ContentContainer
from zojax.portal.interfaces import IPortal

from zojax.harvest.rss import _
from zojax.harvest.rss.interfaces import IHarvestedRSSWorkspace, \
    IHarvestedRSSWorkspaceFactory, IHarvestedRSSItem
from zojax.harvest.rss.item import HarvestedRSSItem
from zope.lifecycleevent import ObjectCreatedEvent
from zope.app.container.interfaces import INameChooser
from zope.security.proxy import removeSecurityProxy
from zope.app.container.contained import ObjectAddedEvent
import BeautifulSoup

import transaction
import feedparser


class HarvestedRSSWorkspace(ContentContainer):
    interface.implements(IHarvestedRSSWorkspace)

    title = _('Harvested RSS')
    __name__ = u'harvested-rss'

    feeds = FieldProperty(IHarvestedRSSWorkspace['feeds'])

    def harvest(self):
        feeds = self.feeds
        if not feeds:
            return 0
        existingIDs = set()
        for obj in self.values():
            item = IHarvestedRSSItem(obj, None)
            if item:
                existingIDs.add(item.id)
        cnt = 0
        for feed in feeds:
            try:
                parsed = feedparser.parse(feed)
                for entry in parsed.entries:
                    if entry.id in existingIDs:
                        continue
                    item = HarvestedRSSItem()
                    item.id = entry.id
                    item.feedURL = str(feed)
                    item.url = str(entry.link)
                    item.title = entry.title
                    summary = getattr(entry, "summary", None)
                    if summary:
                        soup = BeautifulSoup.BeautifulSoup(summary)
                        soup.find("div", {"class": "feedflare"}).extract()
                        summary = unicode(soup)
                        item.summary = summary
                    
                    item.author = getattr(entry, "author", None)
                    item.published = getattr(entry, "published", getattr(entry, "created", None))
                    event.notify(ObjectCreatedEvent(item))
                    name = INameChooser(self).chooseName(u"", item)
                    self[name] = item
                    cnt += 1
            except:
                import logging, traceback
                logging.error(traceback.format_exc())
                continue 
        return cnt


class HarvestedRSSWorkspaceFactory(WorkspaceFactory):
    component.adapts(ISpace)
    interface.implements(IHarvestedRSSWorkspaceFactory)

    name = 'harvested-rss'
    title = _(u'Harvested RSS')
    description = u''
    weight = 9
    factory = HarvestedRSSWorkspace
   

def harvest():
    db = component.getUtility(IDatabase)
    conn = db.open()
    root = conn.root().data['Application']

    portal = IPortal(root, None)
    if portal is None:
        # Old instance of zojax where portal is not the root object.
        # We get the first instance of IPortal if it exists.
        for obj in root.values():
            portal = IPortal(obj, None)
            if portal is not None:
                break
    if portal is None:
        conn.close()
        return
    
    setSite(portal)

    catalog = component.getUtility(ICatalogConfiglet, context=portal).catalog
    workspaces = catalog.searchResults(type={'any_of': ('contenttype.rss.workspace',)})
    try:
        for workspace in workspaces:
            if workspace.harvest():
                transaction.commit()
            else:
                transaction.abort()
    except:
        transaction.abort()
        
    conn.close()

task = LoopTask(harvest, interval=3600*6)

gsm = component.getGlobalSiteManager()
gsm.registerUtility(task, ITask, 'zojax.harvest.rss.harvest', event=False)


