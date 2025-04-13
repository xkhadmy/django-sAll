from django.shortcuts import render 


from django.core.mail import send_mail

import os

def contact_form_view(request):
    if request.method == "POST":
        vorname = request.POST.get("vorname")
        nachname = request.POST.get("nachname")
        email = request.POST.get("email")
        telephone = request.POST.get("telephone")
       
        # Составляем текст письма
        subject = "Neue Kontaktanfrage"
        message = f"""
                Neue Kontaktanfrage von der Website:

                Vorname: {vorname}
                Nachname: {nachname}
                Telefon: {telephone}
                E-Mail: {email}
                """

        recipient_list = ["levitchinicolai527@gmail.com"]

        send_mail(subject, message, os.getenv("EMAIL_HOST_USER"), recipient_list)

        return render(request, 'thank_you.html')  # после отправки

    return render(request, "contact.html")  # форма отображается

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def referenzen(request):
    return render(request, 'referenzen.html')

def offene_stellen(request):
    return render(request, 'offene_stellen.html')

def datenschutz(request):
    return render(request, 'datenschutz.html')

def impressum(request):
    return render(request, 'impressum.html')

def schalung(request):
    return render(request, "schalung.html")

def umbau(request):
    return render(request, "umbau.html")