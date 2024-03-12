import requests

url = 'https://google-translate1.p.rapidapi.com/language/translate/v2'

payload = { "q": "English is hard, but detectably so"}
headers ={    
    'content-type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'application/gzip',
    'X-RapidAPI-Key': '507641d4f3mshe76c5e6c0ec0576p17ebf2jsnc06e22bebe8d',
    'X-RapidAPI-Host': 'google-translate1.p.rapidapi.com'
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())

