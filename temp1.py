import unittest
from ddt import ddt, data



@ddt
class FooTestCase(unittest.TestCase):
    @data(3, 4, 12, 23)
    def test_larger_than_two(self, value):
        print(value)

    @data(1, -3, 2, 0)
    def test_not_larger_than_two(self, value):
        # self.assertFalse(larger_than_two(value))
        print(value)

    @data(u'ascii', u'non-ascii-\N{SNOWMAN}')
    def test_unicode(self, value):
        self.assertIn(value, (u'ascii', u'non-ascii-\N{SNOWMAN}'))


if __name__ == '__main__':
    unittest.main(verbosity=2)