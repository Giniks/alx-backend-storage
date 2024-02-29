import requests
import redis
from functools import wraps

store = redis.Redis()


def cache_and_track_url_access(method):
    """ Decorator counting how many times a URL is accessed and caching the result """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        try:
            html = method(url)
            store.incr(count_key)
            store.set(cached_key, html)
            store.expire(cached_key, 10)
            return html
        except requests.RequestException as e:
            # Handle potential errors from the HTTP request
            print(f"Error accessing URL {url}: {e}")
            return ""

    return wrapper


@cache_and_track_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a URL """
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an exception for HTTP errors
        return res.text
    except requests.RequestException as e:
        # Handle potential errors from the HTTP request
        print(f"Error accessing URL {url}: {e}")
        raise  # Re-raise the exception to propagate it further


