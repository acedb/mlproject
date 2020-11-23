from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r

if __name__ == "__main__":
    # Le Wagon location
    lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    lat2, lon2 = 48.871604158433065, 2.3696945268085834
    distance = haversine(lon1, lat1, lon2, lat2)
    print(distance)
