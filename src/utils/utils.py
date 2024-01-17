# ===
import os
import re

from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
from pillow_heif import register_heif_opener


def getFileNames(folder_name):
    """
    Given a folder location, extract all filenames that are pictures (.heic, .jpg, .jpeg)
    """
    files = [file for file in os.listdir(folder_name)]

    r = re.compile(".*heic|.*HEIC")
    heic_files = list(filter(r.match, files))
    r = re.compile(".*jpg|.*jpeg|.*JPG|.*JPEG")
    jpx_files = list(filter(r.match, files))

    picture_files = heic_files + jpx_files
    return picture_files

def getMetadata(image_file):
    """
    Function opens the file and extracts its datetime stamps and EXIF data. Compatible
    files are: .heic, .jpg, .jpeg. 
    image_file - input file, which metadata needs to be extracted

    Data from exif_data object has following format:
    -- {34853: 2154, 296: 2, 34665: 214, 271: 'Apple', 272: 'iPhone 11', 305: '15.7', 274: 1, 
        306: '2022:10:15 13:45:55', 282: 72.0, 283: 72.0, 316: 'iPhone 11'}
    -- required tags: 306: DateTime

    Data gps_ifd object will be in following format:
    -- {1: 'N', 2: (46.0, 35.0, 52.54), 3: 'E', 4: (10.0, 19.0, 40.39), 5: b'\x00', 6: 2589.9123222748817, 
        12: 'K', 13: 0.26934084300661676, 16: 'T', 17: 173.67962645321137, 23: 'T', 24: 173.67962645321137, 
        29: '2022:10:15', 31: 23.152112536529792}
    
    -- required tags: 1: GPSLatitudeRef, 2: GPSLatitude, 3: GPSLongitudeRef, 4: GPSLongitude

    Required data is:
    1: 'N', 2: (46.0, 35.0, 52.54)
    3: 'E', 4: (10.0, 19.0, 40.39)
    306: '2022:10:15 13:45:55'
    """

    image_metadata = []

    register_heif_opener() # runs method, needed for opening HEIC file format
    image = Image.open(image_file) # creates object that contains opened image file
    image.close()
    exif_data = image.getexif() # extracts exif data
    gps_ifd = exif_data.get_ifd(ExifTags.IFD.GPSInfo) # get GPS info
    
    if gps_ifd.__class__.__name__ == "dict" and len(gps_ifd) == 0:
        print(f">> no EXIF data were found for {image_file}")
        image_metadata = ["no EXIF"]
    else:
        for key, value in gps_ifd.items():
            if GPSTAGS.get(key) in ["GPSLatitudeRef", "GPSLatitude", "GPSLongitudeRef", "GPSLongitude"]:
                image_metadata.append(value)

        for key, values in ExifTags.TAGS.items():
            if values == "DateTime":
                image_metadata.append(exif_data[key])

    return image_metadata

def convertDMStoDD(direction, coordinates):
    """
    EXIF contains coordinates in DMS format, which needs to be converted to DD. 
    As per https://gsp.humboldt.edu/olm/Lessons/GIS/01%20SphericalCoordinates/Reporting_Geographic_Coordinates.html,
    general formula is: DD = Degrees + (Minutes/60) + (Seconds/3600).
    - Latitudes in the southern hemisphere are negative while longitudes in the western hemisphere (where most of the US is) are negative.
    Input is as follows:
    ['N', [46.0, 35.0, 52.54]]
    """
    
    DD = float(round(float(coordinates[0]) + float(coordinates[1])/60 + float(coordinates[2])/3600, ndigits=6))
    if direction.upper() in 'WS':
        DD *= -1
    return str(f"{DD}{direction}")

# === could be done with Typevar https://docs.python.org/3/library/typing.html#typing.TypeVar
class ImageData():
    """
    Create class that will hold following metadata (of a picture):
    - orientation (N, S, E, W)
    - coordinates 
    - date and time, when picture was taken
    """
    def __init__(self, orientationNS, coordinatesNS, orientationEW, coordinatesEW, creationDateTime):
        self.orientationNS = orientationNS
        self.coordinatesNS = coordinatesNS
        self.orientationEW = orientationEW
        self.coordinatesEW = coordinatesEW
        self.creationDateTime = creationDateTime

    def __repr__(self):
        return f"Picture was taken on {self.creationDateTime}, near {self.coordinatesNS}{self.orientationNS} and {self.coordinatesEW}{self.orientationEW}"

