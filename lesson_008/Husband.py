from Human import Human
from House import House
from random import randint

class Husband(Human):

    def __init__(self, name):
        super().__init__(name=name)


    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, super().__str__())

    def act(self):
        monet = randint(1, 10)
        self.claen_house()
        if self.richness <=0 and self.happiness>0:
            print('{} умер'.format(self.name))
            exit()
        elif self.richness <=20:
            self.eat()
        elif self.house.money <= 200:
            self.work()
        elif monet< 8:
            self.gaming()
        elif monet>=8:
            self.work()
        else:
            print('EROR!')


    def work(self):
        self.richness -= 10
        self.house.money += 150
        print('{} сходил на работу!'.format(self.name) if self.richness>0
              else '{} умер на работе!'.format(self.name))


    def gaming(self):
        self.richness -= 10
        self.happiness += 20
        print('{} победил в WoT!'.format(self.name) if self.richness>0
              else '{} умер, но победил в WoT !'.format(self.name))


if __name__ == '__main__':
    f = Husband(name='Кирилл')
    home = House()

    print(f)
    f.go_to_house(home)
    print(home)
    f.work()
    f.work()
    print(f)
    print(home)
    f.gaming()
    print(f)
    f.eat()
    print(f)
    f.work()
    print(f)
    f.act()
    print(f)