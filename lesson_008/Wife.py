from Human import Human
from House import House
from random import randint

class Wife(Human):

    def __init__(self, name):
        super().__init__(name=name)
        self.number_fur_coats = 0

    def __str__(self):
        return '{} {}'.format(self.__class__.__name__, super().__str__())

    def act(self):
        monet = randint(1, 10)
        if self.richness <= 0:
            print('{} умер'.format(self.name))
            exit()
        elif self.house.food <= 30:
            self.shopping()
        elif self.richness <= 20:
            self.eat()
        elif 50 < self.house.dirt < 100:
            self.clean_house()
        elif monet >= 7:
            self.buy_fur_coat()

    def shopping(self):
        self.richness -= 10
        if self.house.money >=30:
            self.house.money -= 30
            self.house.food += 30
            print('{} купила 30 еды!'.format(self.name))
        else:
            if self.house.money >= 10:
                piece = randint(10, self.house.money)
                self.house.food += piece
                self.house.money -= piece
                print('{} купила {} еды!'.format(self.name, piece))
            else:
                piece = self.house.money
                self.house.food += piece
                self.house.money -= piece
                print('{} купила {} еды!'.format(self.name, piece))

    def buy_fur_coat(self):
        if self.house.money >=150:
            self.richness -= 10
            self.happiness += 60
            self.number_fur_coats += 1
            self.house.money -= 150
            print('{} купила шубу!'.format(self.name))
        else:
            print('{} хотела купить шубу, но денег в доме нет!'.format(self.name))

    def clean_house(self):

        self.richness -= 10
        self.house.dirt -= randint(10,100)
        if self.house.dirt <0:
            self.house.dirt = 0
        print('{} убралась!'.format(self.name) if self.richness >0 else
        '{} умерла убираясь!' )



if __name__ == '__main__':
    f = Wife(name='Надежда')
    home = House()

    print(f)
    f.go_to_house(home)
    print(home)
    f.shopping()
    print(f)
    print(home)
    f.buy_fur_coat()
    f.clean_house()
