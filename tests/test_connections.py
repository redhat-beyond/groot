import urllib.request
import pytest

SITE_LOCATION = "http://localhost:5000"

def test_connection():
    assert urllib.request.urlopen(SITE_LOCATION).getcode() == 200
