class vehicle:
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage

model = vehicle(240, 18)
print('The top speed is', model.speed)
print('Milegae is', model.mileage)