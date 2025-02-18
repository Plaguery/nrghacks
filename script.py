import requests
from mailjet_rest import Client
import vars
def getInsult():
    x = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data = x.json()
    insult = data.get("insult")
    return insult

def addMailList(email):
    data = {
        'Email': email
    }
    result = mailjet.contact.create(data=data)
    print(result.status_code)
    print(result.json())


def sendEmail():
    


# Get your environment Mailjet keys
api_key = vars.apiKey
api_secret = vars.secretKey
mailjet = Client(auth=(api_key, api_secret))

insult = getInsult()
data = {
	'FromEmail': '$SENDER_EMAIL',
	'FromName': '$SENDER_NAME',
	'Subject': 'Your email flight plan!',
	'Text-part': '$insult',
	'Html-part': '<h3>Dear passenger, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!<br />May the delivery force be with you!',
	'Recipients': [{'Email': 'sophiayan111@gmail.com'}]
}





# result = mailjet.send.create(data=data)



