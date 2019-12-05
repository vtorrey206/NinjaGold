from django.shortcuts import render, HttpResponse, redirect #import these everytime
import random 
#this is connected to page 1
 

def index(request):
    if 'gold' not in request.session:
         request.session['gold'] = 0
    return render(request,'ninja_gold_app/index.html')
    
def process_money(request):
    if request.POST['building'] =='farm':
        request.session['gold'] += random.randint(10,20)
    if request.POST['building'] =='cave':
        request.session['gold'] += random.randint(5,10)
    if request.POST['building'] == 'house':
        request.session['gold'] += random.randint(2,5)
    if request.POST['building'] == 'casino':
        request.session['gold'] += random.randint(-50,50)
    return redirect('/')

