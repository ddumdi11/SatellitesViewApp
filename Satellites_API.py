import requests

url = "https://uphere-space1.p.rapidapi.com/user/visible"

querystring = {"lat":"32.1433","lng":"-117.9833"}

headers = {
    'x-rapidapi-key': "8995eeaffemshf418b001fb71822p1a5542jsn6785e213a9bc",
    'x-rapidapi-host': "uphere-space1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)