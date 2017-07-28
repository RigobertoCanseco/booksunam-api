import urllib
import urllib2
from urllib2 import URLError, HTTPError
from urllib import urlencode


class HttpConnection:

    def __init__(self):
        pass

    @staticmethod
    def get_request(url, headers=None, parameters=None):
        # urllib2.quote().encode()
        # urllib2.unquote().decode('utf-8')
        # result = urllib2.urlopen(url.encode('utf-8')).read()
        # data = urllib.urlencode({'name' : 'joe','age'  : '10'})
        try:
            if type(parameters) is str:
                url = url + '?' + parameters
            if headers is not None:
                req = urllib2.Request(url, headers=headers)
            else:
                req = urllib2.Request(url)

            req.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
            response = urllib2.urlopen(req, timeout=300)
            return response.read()
        except HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            return None
        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            return None
        except Exception as e:
            return None

    @staticmethod
    def post_request(url, body, headers=None, parameters=None):
        try:
            if type(parameters) is str:
                url = url + '?' + parameters
            data = urllib.urlencode(body)
            if headers is not None:
                req = urllib2.Request(url, data=data, headers=headers)
            else:
                req = urllib2.Request(url, data=data)

            req.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
            response = urllib2.urlopen(req, timeout=300)
            return response.read()
        except HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
            return None
        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
            return None
        except Exception as e:
            return None
