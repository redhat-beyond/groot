import urllib.request
import pytest

SITE_LOCATION = "http://localhost:5000"


def connection():
    try:
        urllib.request.urlopen(SITE_LOCATION)
        return True
    except:
        return False
