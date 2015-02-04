from django.shortcuts import render
from django.http import HttpResponse
# from pages.forms import EmailForm
from pages.models import Email

import json

<<<<<<< HEAD
def home_page(request,name):
    if name=='cogo':
        product = 'Cogo'
    elif name=='ketch':
        product = 'Ketch'

    context = {'name':product}
    return render(request, 'index.html', context)

def submit_email(request,name):
    response_data = {}
    if request.method == 'POST':
        # form = EmailForm(request.POST)
        form_email = request.POST.get('email')
        email = Email(address=form_email, site=name)
        # print email.address # sanity check
        email.save()

        response_data['result'] = 'Submit email successful!'

        return HttpResponse(          
            json.dumps(response_data),
            content_type="application/json"
        )

    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )





