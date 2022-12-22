class Piglet:
    name = "piglet"
    def speak(self):
        print("oink! I'm {}! Oink!". format(self.name))
    years = 0
    def pig_years(self):
        return self.years * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
