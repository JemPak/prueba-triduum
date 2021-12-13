# rest_frameworks imports
from rest_framework           import generics, status
from rest_framework.response  import Response

#import shortcuts 
from django.core.exceptions import ObjectDoesNotExist

# import datetime for update 
from datetime import datetime

# serializers and models import
from apps.search.models       import Search
from apps.search.serializers  import SerializerSearch


class CreateSearch(generics.CreateAPIView):
  serializer_class  = SerializerSearch
  queryset          = Search.objects.all()

  def post(self, request, *args, **kwargs):
    """ Generic does hard word, creates model 
        with user-submitted parameters
    """
    try:
      # get word sent by user, conver to lowercase and strip blank spaces
      word = request.data['word'].strip().lower()
      search = Search.objects.get(word=word)
      search.searchs += 1 #update search increasing 1
      search.lastSearch = datetime.now()
      search.save()
      return Response("Busqueda encontrada y actualizada", status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
      # if Not Exists, create new Search with this params
      return self.create(request, *args, **kwargs)

