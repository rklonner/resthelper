from unittest import TestCase

from resthelper.utils import build_restful_url

class TestBuidlUrl(TestCase):
    def test_is_restful_https_url(self):
        url = build_restful_url('https://jenkins1.tttech.com', 'testuser',  '/rest/1.0/request')
        self.assertEqual(url, 'https://testuser@jenkins1.tttech.com/rest/1.0/request')

    def test_is_restful_http_url(self):
        url = build_restful_url('http://jenkins1.tttech.com', 'testuser',  '/rest/1.0/request')
        self.assertEqual(url, 'http://testuser@jenkins1.tttech.com/rest/1.0/request')

if __name__ == '__main__':
    unittest.main()