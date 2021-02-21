from django.shortcuts import render

# Create your views here.
def chat_view(request, *args, **kwargs):
	print(request.path)
	return render(request, "chat/math.html", {})



# Create your views here.

