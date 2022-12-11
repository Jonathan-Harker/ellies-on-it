import os
import unittest
from os.path import join

from infrastructure.local_persitence import LocalPersistence


class TestLocalPersistence(unittest.TestCase):
    def test_read(self):
        os.environ["DATA_PATH"] = join("resources", "data.pkl")
        persistence = LocalPersistence()
        persistence.read_pkl_file()
