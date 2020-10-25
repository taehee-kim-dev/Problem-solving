class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.status = [None, [0, big], [0, medium], [0, small]]

    def addCar(self, carType: int) -> bool:
        if self.status[carType][0] < self.status[carType][1]:
            self.status[carType][0] += 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
