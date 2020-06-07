import pytest
import sys, os


sys.path.append(os.path.realpath(os.path.dirname(__file__) + "/.."))

from run import app

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client