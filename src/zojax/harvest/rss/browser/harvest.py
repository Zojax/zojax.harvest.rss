from zope import interface, schema, component
from zope.app import zapi

from z3c.form.button import buttonAndHandler

from z3ext.content.actions.action import Action
from z3ext.content.actions.interfaces import IAction, IManageContentCategory
from z3ext.layoutform.field import Fields
from z3ext.layoutform.form import PageletForm
from z3ext.statusmessage.interfaces import IStatusMessage

from zojax.harvest.rss import _
from zojax.harvest.rss.interfaces import IHarvestedRSSWorkspace


class HarvestForm(PageletForm):

    label = _(u'Harvest')
    ignoreContext = True

    @buttonAndHandler(_('Harvest'))
    def handleHarvest(self, action):
        data, errors = self.extractData()
        if errors:
            IStatusMessage(self.request).add(_('Please fix indicated error.'), 'warning')
            return
        else:
            cnt = self.context.harvest()
            IStatusMessage(self.request).add(_('%i items were harvested.' % cnt))
            return


class IHarvestAction(IAction):
    pass


class HarvestAction(Action):
    component.adapts(IHarvestedRSSWorkspace, interface.Interface)
    interface.implements(IHarvestAction, IManageContentCategory)
    
    weight = 50
    title = _('Harvest')
    permission = 'zope.ManageServices'

    @property
    def url(self):
        return '%s/%s'%(zapi.absoluteURL(self.context, self.request), 'harvest')

    
    
