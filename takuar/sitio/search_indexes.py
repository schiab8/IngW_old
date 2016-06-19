from haystack import indexes
from sitio.models import Event, Local

class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='eventName')
    startTime = indexes.DateTimeField(model_attr='startTime')

    def get_model(self):
        return Event
    
    def index_queryset(self,using=None):
        return self.get_model().objects.all()

class LocalIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    idType = indexes.CharField(model_attr='idType')

    def get_model(self):
        return Local

    def index_queryset(self,using=None):
        return self.get_model().objects.all()
