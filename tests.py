import urllib.request

SITE_LOCATION = "http://localhost:5000"


def url_ok(url):
    try:
        r = urllib.request.urlopen(url).getcode()

    except:
        r = 404

    return r

print(url_ok(SITE_LOCATION))
