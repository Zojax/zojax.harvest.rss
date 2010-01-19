from zope import interface, schema
from zope.schema._bootstrapinterfaces import IFromUnicode


class IFeedsField(interface.Interface):
    pass


class FeedsField(schema.Set):
    interface.implements(IFeedsField)
    
