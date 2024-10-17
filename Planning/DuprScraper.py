## need to translate to dart
## need to bypass captcha - but its super simple captchas 
import requests
import bs4 import BeautifulSoup

loginurl = ("https://api.dupr.gg/auth/v1.0/login")
secure_url = ("https://api.dupr.gg/player/v1.0/search")

#create a dic
payload = {
  'username': "REDACTED"
  'password': "REDACTED"
}

searchLoad = {
  'exclude':[]
  'filter': {lat: 29.7604267, lng: -95.3698028, rating: {maxRating: null, minRating: null}, locationText: ""}
  'includeUnclaimedPlayers': true
  'limit': 10
  'offset': 0
  'query': "jonathan"
  
}

with requests.session() as s:
  s.post(loginurl, data = payload)
  r = s.get(s.post(secure_url, data = searchPayload))
  soup = BeautifulSoup(r.content, 'html.parser')
  #soup.prettify?


#this method deprecaites the session so i cant access any new pages
r = requests.post(loginurl, data = payload)




#auth link to send POST request
https://api.dupr.gg/auth/v1.0/login

email: "##Redacted##"
password:  "##Redacted##"

