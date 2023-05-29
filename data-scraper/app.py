import argparse
import requests
import os
from bs4 import BeautifulSoup
import json
from geopy.geocoders import GoogleV3

def load_env_variables():
    env_file = '.env'
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key] = value

# Load environment variables from .env file
load_env_variables()

def geocode_entities(entities):
    api_key = os.environ.get('GMAP_API_KEY')
    geolocator = GoogleV3(api_key=api_key)

    for entity in entities:
        address = entity.get('address', '')
        city = entity.get('city', '')
        state = entity.get('state', '')
        address_string = f"{address}, {city}, {state}"

        try:
            location = geolocator.geocode(address_string)
            if location:
                entity['lat'] = location.latitude
                entity['lng'] = location.longitude
        except Exception as e:
            print(f"Geocoding error for {address_string}: {e}")

    return entities


def scrape_cannabis_locations():
    # Send a GET request to the URL
    url = 'https://cannabis.ny.gov/dispensary-location-verification'
    response = requests.get(url)

    # Create BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the location data
    table = soup.find('table')

    # Initialize a list to store the extracted address information
    address_list = []
    num_delivery_only = 0

    # Iterate over each table row (excluding the header row)
    rows = table.find_all('tr')[1:]
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 6:
            entity_name = cells[0].find('p').get_text(strip=True)
            address = cells[1].find('p').get_text(strip=True)
            city = cells[2].find('p').get_text(strip=True)
            state = cells[3].find('p').get_text(strip=True)
            zip_code = cells[4].find('p').get_text(strip=True)

            # Check if the entity name is suffixed by "***"
            delivery_only = entity_name.endswith('***')

            # Remove the "***" suffix from the entity name if present
            if delivery_only:
                entity_name = entity_name[:-3].strip()

            # Create a dictionary for the extracted address information
            address_info = {
                'name': entity_name,
                'city': city,
                'state': state,
                'address': address,
                'zipCode': zip_code,
                'deliveryOnly': delivery_only
            }

            # Increment delivery-only count if applicable
            if delivery_only:
                num_delivery_only += 1
                del address_info["zipCode"]
                del address_info["address"]

            # Append the address information to the list
            address_list.append(address_info)

    dispensaries = geocode_entities(address_list)

    # Create the final JSON output structure
    json_output = {
        'numDeliveryOnly': num_delivery_only,
        'numDispensaries': len(address_list) - num_delivery_only,
        'dispensaries': dispensaries
    }

    return json_output


if __name__ == '__main__':
    # Create a parser for command-line arguments
    parser = argparse.ArgumentParser(description='Scrape cannabis locations')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Scrape and process the cannabis locations
    json_output = scrape_cannabis_locations()

    # Output the result in the desired format
    print(json.dumps(json_output, indent=4))
