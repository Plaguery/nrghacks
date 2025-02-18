import requests
from mailjet_rest import Client
import vars

#gets random insult
def getInsult():
    x = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data = x.json()
    insult = data.get("insult")
    return insult



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
    


#sends insult email
def sendInsult(email):
    sendEmail("INSULT", getInsult(), email)

    


# setups env
api_key = vars.apiKey
api_secret = vars.secretKey
mailjet = Client(auth=(api_key, api_secret))

sendInsult("teeresa.zhang@gmail.com")



def getClients():
    result = mailjet.contact.get()
    print(result.status_code)
    print(result.json())
    return result

def addMailList(email):
    data = {
        'Email': email
    }
    result = mailjet.contact.create(data=data)
    print(result.status_code)
    print(result.json())
