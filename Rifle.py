from random import randint, randrange


class Rifle(object):
    """
    This class is an abstraction for automated and semi-automated rifles
    with implemented equality methods
    """
    def __init__(self, caliber=None, barrel_length=None, bullet_speed=None):
        self._caliber = caliber if caliber else randint(56, 127) / 10
        self._barrel_length = barrel_length if barrel_length else randrange(2065, 7400, 5) / 10
        self._bullet_speed = bullet_speed if bullet_speed else randrange(310, 900, 5)

    def print_characteristics(self):
        print(f"Caliber: {self._caliber:4.1f} mm; Barrel length: {self._barrel_length:5.1f} mm; "
              f"Bullet speed: {self._bullet_speed:3d} m/s")

    def __eq__(self, other):
        if isinstance(other, Rifle):
            return (self._caliber == other._caliber and
                    self._bullet_speed == other._bullet_speed and
                    self._barrel_length == other._barrel_length)
        return False

    def __lt__(self, other):
        if not isinstance(other, Rifle):
            return False
        if self._caliber == other._caliber:
            return (self._bullet_speed * self._barrel_length) < (other._bullet_speed * other._barrel_length)
        else:
            return self._caliber < other._caliber
