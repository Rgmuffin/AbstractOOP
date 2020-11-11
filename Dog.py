from Animal import Animal


class Dog(Animal):
    def __init__(self):
        print("Dog was created")
        self.is_feed = False

    def feed(self, food):
        if food == "meat":
            self.is_feed = True
            print("Woof")
        else:
            print("Dog's eat only meat!")

    def need_to_feed(self):
        super().need_to_feed()
