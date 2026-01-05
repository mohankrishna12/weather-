import requests

def weather_agent(city: str):
    API_KEY = "e31dfd1ff6b676bbbd78903d3d0e7305"
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )
    response = requests.get(url)
    return response.json()

