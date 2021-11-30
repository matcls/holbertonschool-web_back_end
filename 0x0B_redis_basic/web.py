#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker."""
from functools import wraps
from typing import Callable

import redis
import requests

r = redis.Redis()


def count(method: Callable) -> Callable:
    """Count the number of times a URL is called."""

    @wraps(method)
    def wrapper(*args, **kwds):
        """Wrapper function."""
        r.incr("count:" + args[0])
        page = r.get(args[0])
        if not page:
            page = method(*args, **kwds)
            r.setex(args[0], 10, page)
        return page

    return wrapper


@count
def get_page(url: str) -> str:
    """Return the HTML content of the URL."""
    return requests.get(url).text
