from zope import interface

from zojax.content.model.model import ViewModel

from interfaces import IHarvestedRSSModel


class HarvestedRSSModel(ViewModel):
    interface.implements(IHarvestedRSSModel)
