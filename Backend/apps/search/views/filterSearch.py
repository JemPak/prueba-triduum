# rest_frameworks imports
from rest_framework           import generics, status
from rest_framework.response  import Response

#import shortcuts 
from django.core.exceptions import ObjectDoesNotExist

# serializers and models import
from apps.search.models       import Search
from apps.search.serializers  import SerializerSearch

class FirstSearch(generics.RetrieveAPIView):
  serializer_class = SerializerSearch
  queryset = Search.objects.all()

  def get(self, request, *args, **kwargs):
    queryset = Search.objects.order_by("createSearch").first()
    serializer = SerializerSearch(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


class LastSearch(generics.RetrieveAPIView):
  serializer_class = SerializerSearch
  queryset = Search.objects.all()

  def get(self, request, *args, **kwargs):
    queryset = Search.objects.order_by("lastSearch").last()
    print(queryset)
    serializer = SerializerSearch(queryset, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

class MostSearch(generics.ListAPIView):
  serializer_class = SerializerSearch

  def get_queryset(self):
    # get most search results
    queryset = Search.objects.order_by('searchs').reverse()[:5]
    return queryset


class TotalSearch(generics.RetrieveAPIView):
  serializer_class = SerializerSearch

  def get(self, request, *args, **kwargs):
    queryset = Search.objects.all()
    total_search = 0
    for search in queryset:
      total_search += search.searchs
    respuesta = {"busquedas": total_search}
    return Response(respuesta, status=status.HTTP_200_OK)



