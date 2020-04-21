import urllib.request
import pytest

SITE_LOCATION = "http://localhost:5000"

def test_connection():
    assert urllib.request.urlopen(SITE_LOCATION) == 200 or 201 or 202
