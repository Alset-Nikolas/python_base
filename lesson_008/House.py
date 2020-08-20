
class House:

    def __init__(self, money=100, food=50, dirt=0):
        self.money = money
        self.food = food
        self.dirt = dirt

    def __str__(self):
        return '{}: денег {}, еды {}, грязи {}'.format(
            self.__class__.__name__, self.money, self.food, self.dirt)




home = House()
if __name__ == '__main__':
    print(home)