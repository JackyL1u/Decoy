import requests


def getLocation():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    ip = data['ip']
    city = data['city']
    latitudeLongitude = data['loc'].split(',')
    latitude = latitudeLongitude[0]
    longitude = latitudeLongitude[1]
    locationInfo = [city, ip, latitude, longitude]
    return locationInfo
