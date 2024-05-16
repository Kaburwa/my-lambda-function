import json
import requests

def lambda_handler(event, context):
    # CNBC API endpoint URL
    api_url = "https://api.cnbc.com/v1/quotes/quotes.htm?type=leaders"

    # Make an HTTP GET request to the API endpoint
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON data from the response
        json_data = response.json()

        # Log the JSON data
        print(json.dumps(json_data, indent=4))

        # Return the JSON data
        return json_data
    else:
        # If the request was not successful, log the error
        print("Failed to fetch data from CNBC API")
        return None

