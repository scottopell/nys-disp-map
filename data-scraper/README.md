# Scrape from cannabis.ny.gov
`app.py` can be used to scrape official NY cannabis locations from
https://cannabis.ny.gov/dispensary-location-verification

## Usage
```
$ python3 -m pip install -r requirements.txt
$ python3 app.py --help
usage: app.py [-h] [-o OUTPUT]

Scrape cannabis locations. Writes scraped data to <output> if specified. Requires google maps api key to resolve addresses to lat/lng (aka
geocoding). See `.env.template` for expected env vars

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename. Optional. Uses current date if missing
```

Example output:
```
$ head june_18_2023.json | jq
{
  "numDeliveryOnly": 5,
  "numDispensaries": 10,
  "dispensaries": [
    {
      "name": "Housing Works Cannabis, LLC",
      "city": "New York",
      "state": "NY",
      "address": "750 Broadway",
      "zipCode": "10003",
      "deliveryOnly": false,
      "lat": 40.7302074,
      "lng": -73.99243200000001
    },
    # <snip>
  ]
}
```

## Utilities
### `diff.py`
Use `diff.py` to show a quick summary of the differences between two different versions of the json data emitted from the scraper.

#### Usage/Example
```
$ ./bin/python3 diff.py june_18_2023.json ../src/data.json
Keys only in the first json:  set()
Keys only in the second json:  set()
Values different between the two jsons:  {"root['numDeliveryOnly']": {'new_value': 3, 'old_value': 5}, "root['numDispensaries']": {'new_value': 9, 'old_value': 10}}
Types different between the two jsons:  set()
Lists different between the two jsons:  set() {"root['dispensaries'][12]": {'name': 'Stage One Cannabis LLC', 'city': 'Rensselaer', 'state': 'NY', 'deliveryOnly': True, 'lat': 42.6425794, 'lng': -73.742898}, "root['dispensaries'][13]": {'name': 'Flynnstoned Corporation', 'city': 'Syracuse', 'state': 'NY', 'address': '219 Walton St', 'zipCode': '13202', 'deliveryOnly': False, 'lat': 43.04786989999999, 'lng': -76.1563565}, "root['dispensaries'][14]": {'name': 'Half Island Flavors LLC', 'city': 'Bronx', 'state': 'NY', 'deliveryOnly': True, 'lat': 40.8447819, 'lng': -73.8648268}}
```

Not the worlds cleanest output, but it tells you what you want to know
