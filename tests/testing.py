import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.222.72.134:5000/")
    assert 200 == r.status

    
def test_negative():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.222.72.134:5000/daemon")
    assert r.status == 404


