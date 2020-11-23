# Import from tools
from mlproject.tools import haversine
import pytest

def test_haversine():
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    # My coordinates from google maps here
    lat2, lon2 = 48.871604158433065, 2.3696945268085834
    distance = haversine(lon1, lat1, lon2, lat2)
    assert distance == 1.0474088693924297
