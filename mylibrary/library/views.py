from django.shortcuts import render
from library.models import Car

# Create your views here.
def buy_car(req):
    if req.method == 'POST':
        brand = req.POST.get('brand')
        publish_year = req.POST.get('publish_year')
        colour = req.POST.get('colour')
        mileage = req.POST.get('mileage')
        price = req.POST.get('price')
        Car.objects.create(brand=brand, publish_year=publish_year, colour=colour, mileage=mileage, price=price)
    return render(req, 'index1.html')

def func_name(request):
    if request.method == 'GET':
        lst = Car.objects.all()
        c = {'lst': lst}
    return render(request, 'index2.html', context=c)