import requests
x = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
data = x.json()
print(data.get("insult"))