from Animal import Animal


class Cat(Animal):
    def __init__(self):
        print("Cat was created")
        self.is_feed = False

    def feed(self, food):
        if food == "milk":
            self.is_feed = True
            print("Meow")
        else:
            print("Cat's eat only milk!")

    def need_to_feed(self):
        super().need_to_feed()
