import pytest
from run import app


def test_webserver_running(client):
    assert client.get('/').status_code == 200