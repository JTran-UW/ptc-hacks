from django.shortcuts import render
import string
import random

users = list()
i = int()
code = str()

def subject(url):
	l = len(url)
	url = url[6:l+1]

	return url

def room_code():
	code = str()
	rando = string.ascii_letters
	for i in range(10):
		code += random.choice(rando)
	return code

# Create your views here.
def chat_view(request, *args, **kwargs):
	global i
	global code

	s = subject(request.path)
	if request.method == "POST":
		if i % 2 == 0:
			code = room_code()
		i += 1

		if len(users) > 1:
			return render(request, "chat/chat.html", {"subject": s.capitalize(), "room_code": code})
		else:
			return render(request, "chat/waiting.html", {"subject": s})
	else:
		users.append(request.user)
		return render(request, "chat/waiting.html", {"subject": s})
