import unittest
from organize_pics.src.utils.utils import *

class TestGetFileNames(unittest.TestCase):

    def test_returns_files(self):
        file_names = ["20221015_134554_7730.heic",
                      "20221009_132252_8490.heic",
                      "20221104_103105_9000.jpeg",
                      "20220719_120940_0000.jpeg"]
        self.assertEqual(getFileNames("./organize_pics/tests/images/"), file_names)

class TestGetMetaData(unittest.TestCase):
    
    def test_returns_metadata(self):
        file_names = getFileNames("./organize_pics/tests/images/")
        for j in range(len(file_names)):
            full_string = "./organize_pics/tests/images/" + file_names[j]
            print(getMetadata(full_string))

    def test_no_metadata(self):
        self.assertEqual(getMetadata("./organize_pics/tests/images/20220719_120940_0000.jpeg"), ['no EXIF'])

if __name__ == '__main__':
    unittest.main()

# === bunch of tests: 
# img_metadata = getMetadata("/Users/pb/_coding/python/organize_pics/images/20221015_134554_7730.heic")

# img_test = ImageData(img_metadata[0], img_metadata[1], img_metadata[2], img_metadata[3], img_metadata[4])

# # print(convertDMStoDD(direction=img_test.orientationNS, coordinates=img_test.coordinatesNS))
# # print(convertDMStoDD(direction=img_test.orientationEW, coordinates=img_test.coordinatesEW))

# print(convertDMStoDD(direction="N", coordinates = [50, 3, 59]))
# print(convertDMStoDD(direction="W", coordinates = [5, 42, 53]))

# print(convertDMStoDD(direction="N", coordinates = [58, 38, 38]))
# print(convertDMStoDD(direction="W", coordinates = [3, 4, 12]))

# print(convertDMStoDD(direction="N", coordinates = [41, 49, 55]))