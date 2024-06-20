# Classes are like blueprints for objects. Classes need to be capital Letter
#Self simply represents the object that is created
#Init = Initial

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print('Moves along..')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()



#Super = your gonna inherit, the trademarks, from the parent. So gonna get make and model from OG
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along..')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along..')

class GolfCart(Vehicle):
    pass
#By entering pass, it inherits the original moveset from Vehicles from before, where as other ones
#You specify that its different thats why its different



cessna = Airplane('Cessna', 'Skyhawk', '345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


#Polymorphism = the abiltiy to behave differently, in response to the same input messages

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()

#They all behave differently depending on how they were built