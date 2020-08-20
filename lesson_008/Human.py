from House import House
from random import randint

class Human:

    def __init__(self, name=None, richness=30, happiness=100):
        self.name = name
        self.richness = richness
        self.happiness = happiness
        self.house = None

    def __str__(self):
        return '{}: степень сытости {}, cтепень счастья {}'.format(self.name, self.richness, self.happiness)

    def eat(self):
        if self.house.food >= 30:
            self.richness += 30
            self.house.food -= 30
            print('{} поел 30 еды!'.format(self.name))
        else:
            if self.house.food >= 10:
                piece = randint(10, self.house.food)
                self.richness += piece
                self.house.food -= piece
                print('{} поел {} еды!'.format(self.name, piece))
            else:
                piece = self.house.food
                self.richness += piece
                self.house.food -= piece
                print('{} поел {} еды!'.format(self.name, piece))


    def go_to_house(self, house):
        self.house = house
        print('{} вьехал в дом!'.format(self.name))

    def claen_house(self):
        if self.house.dirt>90:
            self.happiness -=10
            print('{} живет в грязи!'.format(self.name))
        else:
            print('{} рад(аа), что чисто!'.format(self.name))


home = House()

if __name__ == '__main__':
    f = Human(name='Кирилл')
    print(f)
    f.go_to_house(home)
    f.eat()
    print(f)
    print(home)