import http.client
import json

conn = http.client.HTTPSConnection("google.serper.dev")
payload = json.dumps({
  "q": "doğuş üniversitesi çekmeköy",
  "gl": "tr"
})
headers = {
  'X-API-KEY': 'b7715106c7b8f51342a51516b7c413f238773922',
  'Content-Type': 'application/json'
}
conn.request("POST", "/places", payload, headers)
res = conn.getresponse()
data = res.read()


# Load the data into a JSON object
json_data = json.loads(data)

# Loop through each place and print its details
for place in json_data['places']:
    for key, value in place.items():
        print(f"{key}: {value}")
        
    # Add the Google Maps link based on latitude and longitude
    lat = place.get('latitude')
    lon = place.get('longitude')
    if lat and lon:
        google_maps_link = f"https://www.google.com/maps/?q={lat},{lon}"
        print(f"Google Maps Link: {google_maps_link}")
        
    print('-' * 50)  # separator for each place