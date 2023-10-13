import requests
api="https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=49ae2e9c5214489d95f13b5e43087667"
json_data=requests.get(api).json()
print(json_data)