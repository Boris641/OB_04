from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, hit):
        pass

class Sword(Weapon):
    def attack(self, hit):
        print("Боец выбирает меч")
        print("Боец бьёт мечём")
class Bow(Weapon):
    def attack(self, shoots):
        print("Боец выбирает лук")
        print("Боец стреляет из лука")
class A_spear(Weapon):
    def attack(self, throws):
        print("Боец берёт копьё")
        print("Боец метает Копьё")
class Fighter():
    def __init__(self, hit, shoots, victory):
        self.hit = hit
        self.shoots = shoots
        self.victory = victory
    def printer1(self):
        self.victory.attack(self)

    def printer2(self):
        self.victory.attack(self)
    def changeWeapon(self, a_spear):
        self.victory.attack(a_spear)

        print(f"Оружие{a_spear} добавлено в арсенал")


class Monster():
    def __init__(self, defeated):
        self.defeated = defeated

        print("Монстр побежден!")



fighter = Fighter("Меч", "Наносит адар", Sword())
fighter.printer1()
fighter = Fighter("Меч", "Наносит адар", Bow())
monster1 = Monster("Побеждён")
fighter.printer2()
monster2 = Monster("Побеждён")
a_spear = Fighter("Бьёт", "Метает","Побеждает")
fighter.changeWeapon(a_spear)



