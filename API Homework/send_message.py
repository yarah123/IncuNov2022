from flask import Flask, request
import requests
import json
import emoji


bot_name = 'Incubator23@webex.bot'
roomId = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMjljNGRjZDAtOTBmOC0xMWVkLWEyYWYtYmQwM2JkNzRkZDEz'
token = 'OTA4N2ZhOWQtNzZiOC00Y2M1LWJhOWMtNTAxYzNiYzE3NDRmMGFiMTBjOWItZjA5_PE93_f451a09f-5fe6-4b74-a13a-2fde64738081'
header = {"content-type": "application/json; charset=utf-8",
          "authorization": "Bearer " + token}
############## Flask Application ##############
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) #this URL triggers the function below
def sendMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages'
	msg = {"roomId": webhook["data"]["roomId"]}
	sender = webhook["data"]["personEmail"]
	message = getMessage()
	if (sender != bot_name):
		if message.lower() == "help":
				msg["markdown"] = "Welcome to **Grads Bot**!  \n List of available commands: \n- grads \n- help"
		elif message.lower() ==  "hello":
		                msg["markdown"] = 'Hi!😊️'
		elif message.lower() ==  "grads":
		       	msg["markdown"] = 'Python Masters!'
		elif message.lower().startswith("weather "):
			        message_list = message.split()
			        city = message_list[1]
			        url_weather = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&&appid=0333f5210942ef14ff98bfef3d73015a"
			        response_weather = requests.get(url_weather)
			        data1 = response_weather.text
			        parse_json = json.loads(data1)
			        info = parse_json["weather"]
			        msg["markdown"] = str(json.dumps(info,sort_keys=True,indent=2))
		else: 
			msg["markdown"] = "YOU'RE IN TROUBLE! Type **help** to get more information."
	requests.post(url,data=json.dumps(msg,indent=2), headers=header, verify=True)
		#requests.post(url,msg, headers=header, verify=True)

def getMessage():
	webhook = request.json
	url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
	get_msgs = requests.get(url, headers=header, verify=True)
	message = get_msgs.json()['text']
	return message

app.run(debug = True)


