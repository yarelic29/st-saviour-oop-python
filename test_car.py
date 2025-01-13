from car import Car
from sportscar import Sportscar

def test_car():
    my_car = Car(True, True, 4)
    assert my_car.drive('Santa Monica') == 'the car drives to Santa Monica on 4 wheels!'

    assert len(my_car.accessories) == 0
    my_car.add_accessories('dashcam', 'leather interior', 'tinted windows', 'hula girl')
    assert len(my_car.accessories) == 4

def test_sportcar():
    my_sportscar = Sportscar('red', True)
    assert isinstance(my_sportscar, Sportscar)
    assert isinstance(my_sportscar, Car) 

def test_pickup_truck():
    my_pickuptruck = my_pickuptruck (4, weight)
    assert isinstance(my_pickuptruck, Pickuptruck)
    assert isinstance(my_sportscar, Sportscar)
    assert isinstance(my_sportscar, Car)

