import requests

def fetch_data_from_tool(api_url, api_key):
    headers = {'Authorization': f'Bearer {api_key}'}
    response = requests.get(api_url, headers=headers)
    return response.json()
