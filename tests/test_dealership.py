import pytest
import sys
import os
sys.path.append(os.getcwd())

from dealership.models.dealership import Dealership

dealership1 = Dealership("Dealership 1", -1)
dealership2 = Dealership("Dealership 2", 0)
dealership3 = Dealership("Dealership 3", 5)

@pytest.mark.parametrize('input, expected', 
    [(dealership1.capacity, 0), (dealership2.capacity, 0), (dealership3.capacity, 5)])
def test_capacity(input, expected):
    assert input == expected
