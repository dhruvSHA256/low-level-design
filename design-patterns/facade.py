# Facede: Structural pattern
# single api for multiple complex operations

class Cook(object):
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()

        self.boiler = Boiler()
        self.boiler.boilVegetables()

        self.frier = Frier()
        self.frier.fry()


class Cutter(object):
    def cutVegetables(self):
        print("cutting veggies")


class Boiler(object):
    def boilVegetables(self):
        print("boiling veggies")


class Frier(object):
    def fry(self):
        print("frying veggies")


def main():
    cook = Cook()
    cook.prepareDish()


if __name__ == "__main__":
    main()
