import requests

def getForecast(lat: float, lon: float) -> str:
    """
    Get weather forecast for a given latitude and longitude.
    """
    # Step 1: Get gridpoint from lat/lon
    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    points_response = requests.get(points_url)

    if points_response.status_code != 200:
        return "Could not fetch location data."

    points_data = points_response.json()
    forecast_url = points_data['properties']['forecast']

    # Step 2: Get forecast
    forecast_response = requests.get(forecast_url)

    if forecast_response.status_code != 200:
        return "Could not fetch forecast data."

    forecast_data = forecast_response.json()
    periods = forecast_data['properties']['periods']
    forecast_strings = [f"{p['name']}: {p['detailedForecast']}" for p in periods[:3]]  # First 3 periods

    return "\n".join(forecast_strings)
