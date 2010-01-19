from zope import interface
from zojax.product.product import Product
from zojax.harvest.rss.interfaces import IHarvestRSSProduct


class HarvestRSSProduct(Product):
    interface.implements(IHarvestRSSProduct)
        