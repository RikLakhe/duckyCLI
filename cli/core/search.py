import requests

from cli.constants.api import DUCKDUCKGO_API_URL


def search_function(query, limit):
    # Define parameters for the API request
    params = {
        'q': query,
        'format': 'json',
    }

    # Make the API request
    response = requests.get(DUCKDUCKGO_API_URL, params=params)
    if response.status_code == 200:
        # Parse the JSON response
        results = response.json()
        # Extract relevant information from the response
        search_results = []
        for result in results.get('Results', []):
            search_results.append(result.get('FirstURL', ''))

        # Limit the number of results based on the provided limit
        search_results = search_results[:limit]

        return search_results

    else:
        # Print an error message if the request fails
        print(f"Error: Unable to fetch search results. Status code: {response.status_code}")
        return []
