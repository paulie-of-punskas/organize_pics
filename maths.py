# === implement Haversine's formula (https://en.wikipedia.org/wiki/Haversine_formula)
import math

def getDistance(lat1: float, long1: float, lat2:float, long2:float):
    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)
    r = 6371 # Earth's radius in km
    d = 2 * r * math.asin(math.sqrt(math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((long2 - long1) / 2) ** 2))
    return d

print(getDistance(lat1=50.066389, long1=-5.714722, lat2=58.643889, long2=-3.07))
