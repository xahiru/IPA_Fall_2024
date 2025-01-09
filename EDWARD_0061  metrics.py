import requests
import logging

logging.basicConfig(level=logging.INFO)

url = "http://127.0.0.1:8000/api/metrics/"

headers = {"Authorization": "Token 9ee387fa0b9af96fd5d38235fdd3bca5279bfa48"}

def fetch_metrics():
    """Fetch greenhouse metrics data from the API."""
    try:
    
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            logging.info("Metrics data fetched successfully.")
            return response.json()  
        else:
            logging.error(f"Failed to fetch data. Status code: {response.status_code}")
            return None  

    except requests.exceptions.RequestException as e:
        
        logging.error(f"An error occurred while making the request: {e}")
        return None  

if __name__ == "__main__":

    metrics_data = fetch_metrics()

    if metrics_data:
        logging.info("Metrics Data: %s", metrics_data)  
    else:
        logging.error("No metrics data returned.")
