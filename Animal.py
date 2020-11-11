from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name
        self.size = "unknown"
        super().__init__()

    def set_size(self, newsize):
        self.size = newsize

    def get_size(self):
        print(self.size)

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def need_to_feed(self):
        if self.is_feed == False:
            print("Yes")
        else:
            print("No")
