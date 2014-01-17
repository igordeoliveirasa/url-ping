import urllib
import unittest

class Navigator:

    def __init__(self, verbose = True):
        self.verbose = verbose
        self.divisor = "-" * 70

    def ping(self, url):
        f = urllib.urlopen(url)
        code = f.getcode()
        
        if self.verbose:
            print self.divisor
            print "Accessing URL: %s => %d" % (url, code)
            print self.divisor
        
        return code

class TestNavigator(unittest.TestCase):

    def setUp(self):
        self.navigator = Navigator()

    def test_ping_google(self):
        result = self.navigator.ping("http://fgv.herokuapp.com")
        self.assertEquals(result, 200)

if __name__ == '__main__':
    unittest.main()
