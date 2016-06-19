from haystack import indexes
from forum.models import Thread

class ThreadIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    submit_date = indexes.DateTimeField(model_attr='submit_date')

    def get_model(self):
        return Thread

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
