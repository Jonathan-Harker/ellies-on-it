from interfaces.persistence_interface import PersistenceInterface


class PersistenceSpy(PersistenceInterface):
    def __init__(self):
        self.call_stack = []
        self.call_count = 0

    def save_pkl_file(self, **kwargs) -> None:
        self.call_stack.append({"method": "save_pkl_file", "called_with": kwargs})
        self.call_count += 1

    def read_pkl_file(self, *args) -> None:
        self.call_stack.append({"method": "read_pkl_file", "called_with": args})
        self.call_count += 1
