# NYS Dispensary Map

Data is collected from https://cannabis.ny.gov/dispensary-location-verification

Since that website doesn't include a map, and as far as I know there are no other particularly easy ways to find officially licensed dispensaries, here it is.

## Setup
This is a create-react-app static site that uses leaflet/osm to render the map.

Data scraping is done via the python script found in `data_scraper` and geocoding is done by an API call to google maps.

## Deployment
TBD, probably github pages
