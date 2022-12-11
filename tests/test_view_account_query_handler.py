import unittest


class TestViewAccountQueryHandler(unittest.TestCase):
    def test_query_returns_view(self):
        query = ViewAccountQuery()
        handler = ViewAccountQueryHandler()
