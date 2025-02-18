import requests
from mailjet_rest import Client
import vars
import base64

def getInsult():
    x = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data = x.json()
    insult = data.get("insult")
    return insult

def getQuote():
    x = requests.get('https://zenquotes.io/api/random')
    data = x.json()
    if isinstance(data, list) and len(data) > 0:
        quote = data[0].get("q")  # Correct key for the quote
        return quote
    return None

def getFact():
    x = requests.get('https://meowfacts.herokuapp.com/')
    data = x.json()
    fact_list = data.get("data")  # "data" is a list containing the fact(s)
    
    if isinstance(fact_list, list) and len(fact_list) > 0:
        return fact_list[0]
    return None

def getPhoto():
    x = requests.get('https://api.thecatapi.com/v1/images/search')
    data = x.json()
    image_url = data[0]['url']
    return image_url

def addMailList(email):
    data = {
        'Email': email
    }
    result = mailjet.contact.create(data=data)
    print(result.status_code)
    print(result.json())


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

def sendPhotoEmail(subject, photo_url, email):
    data = {
	'FromEmail': vars.senderEmail,
	'FromName': vars.senderName,
	'Subject': subject,
	
	'Html-part': f'<img src="{photo_url}" alt="alternatetext">',
	'Recipients': [{'Email': email}]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)

def sendPhotoEmail(subject, photo_url, email):
    data = {
	'FromEmail': vars.senderEmail,
	'FromName': vars.senderName,
	'Subject': subject,
	
	'Html-part': f'<img src="{photo_url}" alt="alternatetext">',
	'Recipients': [{'Email': email}]
    }
    result = mailjet.send.create(data=data)
    return result.status_code
    
def getClients():
    result = mailjet.contact.get()
    print(result.status_code)
    print(result.json())
    return result

def sendInsult(email):
    return sendEmail("INSULT", getInsult(), email)  

def sendQuote(email):
    return sendEmail("QUOTE", getQuote(), email)

def sendFact(email):
    sendEmail("FACT", getFact(), email)

def sendPhoto(email):
    sendPhotoEmail("PHOTO", getPhoto(), email)
    
# setups env
api_key = vars.apiKey
api_secret = vars.secretKey
mailjet = Client(auth=(api_key, api_secret))

#sendInsult("sophiayan111@gmail.com")
sendPhoto("sophia.guo.1212@gmail.com")
print(getPhoto())

# result = mailjet.send.create(data=data)