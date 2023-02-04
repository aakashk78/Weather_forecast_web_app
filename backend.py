import requests

API_KEY = "b31fb97de23fd7d1937eb1938f569fb6"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    nr_values = 8*forecast_days

    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    get_data()