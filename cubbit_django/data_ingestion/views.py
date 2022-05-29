from data_ingestion.models import Event
from data_ingestion.serializers import EventSerializer
from data_ingestion.cache.cache import CacheService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
import data_ingestion.tasks.jobs


class EventList(APIView, LimitOffsetPagination):

    def get(self, request, format=None):
        """
        List first PAGE_SIZE events
        """
        events = Event.objects.all()
        paginated_events = self.paginate_queryset(events, request, view=self)
        serializer = EventSerializer(paginated_events, many=True)
        return Response(serializer.data)
        
    def delete(self, request, format=None):
        """
        Delete all events
        """
        events = Event.objects.all().delete()
        serializer = EventSerializer(events, many=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, format=None):
        """
        Create a new event
        
        Store the event in cache, check if the cache is full
        and perform the storage on the filesystem
        """
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        cacheService = CacheService.instance()
        cacheService.save(request.data)
        if cacheService.cache_is_full():
            cacheService.bulk_store()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        

