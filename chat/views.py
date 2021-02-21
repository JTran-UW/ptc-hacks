from django.shortcuts import render

# Create your views here.
def chat_view(request, *args, **kwargs):
	s = kwargs.get("subject")
	room_code = kwargs.get("code", None)

	if room_code == None:
		return render(request, "chat/waiting.html", {"subject": s.capitalize()})
	else:
		return render(request, "chat/chat.html", {"subject": s.capitalize(), "room_code": room_code})
