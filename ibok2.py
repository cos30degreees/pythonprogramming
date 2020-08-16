# import the library
import googlemaps
import pprint
import time
import pandas as pd
import geopy
import geopy.distance

# Define starting point.



# Define the API Key.
API_KEY = 'AIzaSyDTMCOmXIfrlJ00QxHem-RTKH3f5ULyMdY'

# Define the Client
gmaps = googlemaps.Client(key=API_KEY)
geocode_result = gmaps.geocode(input("Enter place name:"))
pprint.pprint(geocode_result)

lat = geocode_result[0]["geometry"]["location"]["lat"]
lng = geocode_result[0]["geometry"]["location"]["lng"]

for details in geocode_result[0]["address_components"]:
    if details['types'] == ['postal_code']:
        print("Pin Code:" + details['long_name'])

coord = "\"{0},{1}\"".format(lat,lng)
print(coord)


coord = "{0},{1}".format(lat,lng)
rad = int(input("Enter radius of surrounding[in mts]:"))
typ = input("Enter types of place followed by a space:")


def new_points(lat, long):
    start = geopy.Point(lat, long)
    d = geopy.distance.VincentyDistance(kilometers = 1)

    return d.destination(point=start, bearing=0)


params = {
    'location': coord,
    'radius': rad,
    'type': typ
}
count = 0
stored_results = []
new_stored_results = []
# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters


def extract_places(places_result):
    for place in places_result['results']:
        time.sleep(1)
        # define the place id, needed to get place details. Formatted as a string.
        my_place_id = place['place_id']

        # define the fields you would liked return. Formatted as a list.
        my_fields = ['name', 'formatted_phone_number', 'formatted_address', 'website', 'type', 'geometry/location']
        # make a request for the details.
        places_details = gmaps.place(place_id=my_place_id, fields=my_fields)
        pprint.pprint(places_details)
        name = places_details['result']['name']
        formatted_address = places_details['result']['formatted_address']
        phone_num = places_details['result'].get('formatted_phone_number','None')
        website = places_details['result'].get('website','None')
        place_type = places_details['result']['types']
        placeList = [name, formatted_address, phone_num, website, place_type]
        latlng = places_details['result']['geometry']['location']
        params['location'] = latlng['lat'], latlng['lng']
        print(count)
        stored_results.append(placeList)

    return stored_results

#Loop for next page


def get_new_places():
    places_result = gmaps.places_nearby(**params)
    if 'next_page_token' in places_result:
        while 'next_page_token' in places_result:
            places_result = gmaps.places_nearby(**params)
            print(params)
            new_stored_results = extract_places(places_result)
            if 'next_page_token' in places_result:
                params['page_token'] = places_result['next_page_token']
            else:
                break
    else:
        places_result = gmaps.places_nearby(**params)
        new_stored_results = extract_places(places_result)

    return new_stored_results

new_stored_results = get_new_places()

# -------------- DUMPING VALUES IN EXCEL -----------------------
print("Dumping Values in Excel...")
# define the headers, that is just the key of each result dictionary.
# row_headers = stored_results[0].keys()
# create a new workbook and a new worksheet.
a = pd.DataFrame(new_stored_results, columns=['Name', 'Address', 'Phone Number', 'Website', 'Business Type'])

writer = pd.ExcelWriter(typ + '.xlsx', engine='xlsxwriter')
a.to_excel(writer, sheet_name='ibok leads', index=False)
writer.save()
