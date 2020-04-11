import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.222.72.134/")
    assert 200 == r.status
    



