class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self._spaces = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self._spaces[carType] == 0:
            return False
        self._spaces[carType] -= 1
        return True
