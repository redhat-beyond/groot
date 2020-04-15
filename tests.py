from test_connections import connection
import pytest


def test_conn():
    assert connection(), "test failed since site is not reachable"
