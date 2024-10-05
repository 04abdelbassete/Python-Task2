class Bike:
    def __init__(self, type, manufacturer):
        self.type = type
        self.manufacturer = manufacturer
    

road_bike = Bike('Road bike', 'Razesa')
print(road_bike.type)
print(road_bike.manufacturer)
