# ===
import os
from PIL import Image
from PIL import ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
from pillow_heif import register_heif_opener

image_file = "/Users/pb/_coding/python/organize_pics/images/20221015_134554_7730.heic"
register_heif_opener() # runs method, needed for opening HEIC file format
image = Image.open(image_file) # creates object that contains opened image file
exif_data = image.getexif() # extracts exif data
print(type(exif_data))
print(exif_data.items())

exif_data_items = exif_data.items()
image_metadata = []

gps_ifd = exif_data.get_ifd(ExifTags.IFD.GPSInfo)
for key, value in gps_ifd.items():
    if GPSTAGS.get(key) in ["GPSLatitudeRef", "GPSLatitude", "GPSLongitudeRef", "GPSLongitude"]:
        image_metadata.append(value)

for key, values in ExifTags.TAGS.items():
    if values == "DateTime":
        image_metadata.append(exif_data[key])

print(image_metadata)

# for key, val in exif_data.items():
#     if key in ExifTags.TAGS:
#         print(f'{ExifTags.TAGS[key]}:{val}')

# === get dictionary keys and their values
# for key in ExifTags.TAGS:
#     print(f"{key}, {ExifTags.TAGS[key]}")

# for key, values in ExifTags.TAGS.items():
#     print(f"{key}, {values}")
