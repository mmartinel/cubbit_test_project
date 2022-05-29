from data_ingestion.serializers import EventSerializer
from datetime import datetime, timedelta


class CacheService():
    _instance = None
    _items = []
    _last_bulk_store = None
    _cache_ttl = 30
    _cache_max_items = 100

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            cls._last_bulk_store = datetime.now()
        return cls._instance

    def cache_is_full(self):
        """
        Check if cache is full
        """
        print("cache_is_full - items:", len(self._items))
        return len(self._items) >= 3

    def bulk_store(self):
        """
        Insert cached events into DB table
        """
        print("bulk_store - performing bulk storage...")
        if len(self._items) == 0:
            print("bulk_store - no items in cache")
            return
        serializer = EventSerializer(data=self._items, many=True)
        if serializer.is_valid():
            serializer.save()
            self._items = []
            self._last_bulk_store = datetime.now()
            print("bulk_store - bulk storage performed")

    def save(self, event):
        """
        Save event in cache
        """
        print("save - saving event:", event)
        self._items.append(event)
        print("save - event saved")

    def ttl_is_expired(self):
        """
        Check if cache ttl is expired
        """
        print("ttl_is_expired")
        diff = datetime.now() - self._last_bulk_store
        return diff > timedelta(seconds=self._cache_ttl)

    @classmethod
    def get_cache_ttl(cls):
        """
        Return cache time to live
        """
        return cls._cache_ttl

