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
