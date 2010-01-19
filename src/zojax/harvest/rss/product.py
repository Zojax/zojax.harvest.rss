from zope import interface
from z3ext.product.product import Product
from zojax.harvest.rss.interfaces import IHarvestRSSProduct


class HarvestRSSProduct(Product):
    interface.implements(IHarvestRSSProduct)
        