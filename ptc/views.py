from django.shortcuts import render

# Create your views here
def home(request):
    return render(request, "index.html")


def chat_view(request, *args, **kwargs):
	return render(request, "math.html")

