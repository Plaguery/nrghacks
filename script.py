import requests
from mailjet_rest import Client
import vars

#gets random insult
def getInsult():
    x = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data = x.json()
    insult = data.get("insult")
    return insult

#gets quote
def getQuote():
    x = requests.get('https://zenquotes.io/api/random')
    data = x.json()
    if isinstance(data, list) and len(data) > 0:
        quote = data[0].get("q")  # Correct key for the quote
        return quote
    return None

#sends email 
def sendEmail(subject, content, email):
    data = {
	'FromEmail': vars.senderEmail,
	'FromName': vars.senderName,
	'Subject': subject,
	'Text-part': content,
	'Html-part': f'<h3>{content}</h3>',
	'Recipients': [{'Email': email}]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    
#sends quote
def sendQuote(email):
    sendEmail("QUOTE", getQuote(), email)

#sends insult email
def sendInsult(email):
    sendEmail("INSULT", getInsult(), email)



# setups env
api_key = vars.apiKey
api_secret = vars.secretKey
mailjet = Client(auth=(api_key, api_secret))

#sendInsult("sophiayan111@gmail.com")




# result = mailjet.send.create(data=data)



