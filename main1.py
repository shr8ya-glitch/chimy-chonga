class vehicle:
    def __init__(self,speed,mileage):
        self.speed=speed
        self.mileage=mileage
model=vehicle(120,10000)
print("Speed:",model.speed)
print("Mileage:",model.mileage)