from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def HomePage(request):
  page = "<!DOCTYPE html><html>"
  page += "<head></head>"
  page += "<body>"
  page += "<h3> Hello World! </h3>"
  page += "<p> This is our first Django example! </p>"
  page += "<P><a href='tipper'>The Actual App</a></P>"
  page += "<P><a href='simple'>A Simple Example</a></P>"
  page  += "</body></html>"
  return HttpResponse(page)


def simple(request):
  data = { "title": "Simple Template", "message": "Hello World"}
  return render(request, 'simple.html', data)

def inputs(request):
  return render(request, 'tip_app.html')


def calculateTip(request):
  price = float(request.GET.get("price"))
  satisfaction = int(request.GET.get("satisfaction"))/100
  tip_amount = price * satisfaction
  total = price + tip_amount

  return render(request, "results.html", {"tip_amount": format(tip_amount,".2f"), "total": format(total, ".2f")})