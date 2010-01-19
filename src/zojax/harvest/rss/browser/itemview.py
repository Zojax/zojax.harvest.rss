from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile


class ItemView(object):
    
    template = ViewPageTemplateFile("itemview.pt")
    
    def render(self):
        return self.template()