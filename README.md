## App idea
1. User stores images in one folder
2. App loops through images and extracts their metadata:
- date and time taken,
- location (if available):
    - country
    - nearest (?) town/city

2a. If no date or no locations was found then create corresponding folders:
- _unknown_date
- _unknown_location
- _unknown_both

3. Categorizes the pictures in following pattern:  
`%YEAR%_%MONTH%_%COUNTRY%_%LOCATION%`
- if location is CH, then location is should be name of then Canton, where picture was taken

## Code order/description
- `maths.py`:`
    - contains `getDistance()` method, that is used for calculating distance between two points on Earth

- `utils.py`:
    - `getFileNames()` - retrieves filenames, that are in .jpg, .jpeg or .heic formats
    - `getMetadata()` - extrats GPS data and datetime when image was taken
    - `convertDMStoDD()` - converts data from DMS to DD format

## To do:
1. add more tests
2. create directories according to date and location.
