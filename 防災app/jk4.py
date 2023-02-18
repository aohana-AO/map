import requests

url = "https://mapfanapi-route.p.rapidapi.com/calcroute"

querystring = {"start":"139.76730676,35.68095910","destination":"139.62261961,35.46606942"}

headers = {
	"X-RapidAPI-Key": "2e6ad5fdb1mshf913d7f4fff4046p131407jsncad95252ac8a",
	"X-RapidAPI-Host": "mapfanapi-route.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)