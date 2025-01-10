import requests

# API URL for greenhouse metrics
url = "http://127.0.0.1:8000/api/metrics/"
# Replace with your actual token
headers = {"Authorization": "Token 9ee387fa0b9af96fd5d38235fdd3bca5279bfa48"}

# Send GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print("Metrics Data:", response.json())  # Print the response (greenhouse metrics data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
