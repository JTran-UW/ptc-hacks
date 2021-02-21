import json
import string
import random
from channels.generic.websocket import WebsocketConsumer

users = []
def room_code():
	code = str()
	rando = string.ascii_letters
	for i in range(10):
		code += random.choice(rando)
	return code

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        users.append(self)
        if len(users) == 2:
            rc = room_code()
            for user in users:
                user.send(text_data=json.dumps({
                    "message": rc
                }))

    def disconnect(self, close_code):
        users.remove(self)
