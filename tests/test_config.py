import os


class TestConfig:
    @staticmethod
    def get_test_base_path():
        return os.path.dirname(os.path.realpath(__file__))
