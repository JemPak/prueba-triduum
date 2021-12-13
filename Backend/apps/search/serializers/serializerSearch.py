# import serializers class from rest_framework
from rest_framework     import serializers
# import model search
from apps.search.models import Search 

class SerializerSearch(serializers.ModelSerializer):
  class Meta:
    model = Search
    fields = '__all__'
  
  def to_representation(self, obj):
    """ Override To_representation method
    params:
      obj: Search object to retrieve data
    return 
      dict: object search personalized  
    """
    search = Search.objects.get(word=obj.word)

    return {
      "word":       search.word,
      "searchs":    search.searchs,
      "content":    len(search.result),
      "lastSearch": search.lastSearch 
    }