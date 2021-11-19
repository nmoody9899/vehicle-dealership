import pytest
import sys
import os
sys.path.append(os.getcwd())

from dealership.classes.vehicle import Vehicle

vehicle1 = Vehicle(2002, 'Pontiac', 'Grand Prix', 150000, 5000)
vehicle2 = Vehicle(2002, 'Pontiac', 'Grand Prix', 150000, -1)
vehicle3 = Vehicle(2002, 'Pontiac', 'Grand Prix', -1, 5000)
vehicle4 = Vehicle(2002, 'Pontiac', 'Grand Prix', -1, -1)

@pytest.mark.parametrize('input, expected', 
    [(vehicle1.price, 150000.00), (vehicle2.price, 150000.00), (vehicle3.price, 0.00), (vehicle4.price, 0.00)])
def test_price(input, expected):
    assert input == expected

@pytest.mark.parametrize('input, expected', 
    [(vehicle1.mileage, 5000), (vehicle2.mileage, 0), (vehicle3.mileage, 5000), (vehicle4.mileage, 0)])
def test_mileage(input, expected):
    assert input == expected