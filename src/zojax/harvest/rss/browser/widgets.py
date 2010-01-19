from zope import interface, component

from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.converter import BaseDataConverter
from z3c.form.interfaces import IFormLayer, IFieldWidget, DISPLAY_MODE
from z3c.form.widget import FieldWidget

from zojax.harvest.rss.fields import IFeedsField


class IFeedsWidget(interface.Interface):
    pass


class FeedsWidget(TextAreaWidget):
    interface.implements(IFeedsWidget)


class FeedsWidgetConverter(BaseDataConverter):
    component.adapts(IFeedsField, FeedsWidget)

    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
        
        if self.widget.mode == DISPLAY_MODE:
            return value
            
        if value is self.field.missing_value:
            return u''
        
        return u'\n'.join(value)

    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
        res = set()
        for line in value.split('\n'):
            line = line.strip()
            if line:
                res.add(line)
        return res 


@interface.implementer(IFieldWidget)
@component.adapter(IFeedsField, IFormLayer)
def FeedsFieldWidget(field, request):
    return FieldWidget(field, FeedsWidget(request))