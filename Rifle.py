from random import randint, randrange


class Rifle(object):
    def __init__(self, caliber=None, barrel_length=None, bullet_speed=None):
        self.__caliber = randint(56, 127) / 10
        self.__barrel_length = randrange(2065, 7400, 5) / 10
        self.__bullet_speed = randrange(310, 900, 5)

        if caliber:
            self.__caliber = caliber
        if barrel_length:
            self.__barrel_length = barrel_length
        if bullet_speed:
            self.__bullet_speed = bullet_speed

    def print_characteristics(self):
        print(f"Caliber: {self.__caliber:4.1f} mm; Barrel length: {self.__barrel_length:5.1f} mm; "
              f"Bullet speed: {self.__bullet_speed:3d} m/s")

    def __eq__(self, other):
        if other is self:
            return True
        if not isinstance(other, Rifle) or other is None:
            return False
        if self.__caliber == other.__caliber and self.__bullet_speed == other.__bullet_speed and self.__barrel_length == other.__barrel_length:
            return True
        return False
