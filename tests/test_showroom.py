import pytest
import sys
import os
sys.path.append(os.getcwd())

from dealership.models.showroom import Showroom

showroom1 = Showroom("Showroom 1", -1)
showroom2 = Showroom("Showroom 2", 0)
showroom3 = Showroom("Showroom 3", 5)

@pytest.mark.parametrize('input, expected', 
    [(showroom1.capacity, 0), (showroom2.capacity, 0), (showroom3.capacity, 5)])
def test_capacity(input, expected):
    assert input == expected

