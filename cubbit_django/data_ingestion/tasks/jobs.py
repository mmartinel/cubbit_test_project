from data_ingestion.cache.cache import CacheService
import threading
import time
import schedule


def run_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


def bulk_store_task():
    """
    Perform bulk storage if cache ttl is expired
    """
    cache_service = CacheService.instance()
    if cache_service.ttl_is_expired():
        cache_service.bulk_store()
        

print("scheduling bulk storage")
cache_ttl = CacheService.get_cache_ttl()
schedule.every(cache_ttl).seconds.do(bulk_store_task)

# Start the background thread
stop_run_continuously = run_continuously()  
