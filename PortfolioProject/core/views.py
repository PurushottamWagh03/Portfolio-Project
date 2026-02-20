from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import Profile

def home(request):
    profile = Profile.objects.first()
    return render(request, "core/home.html", {"profile": profile})

def about(request):
    return render(request, "core/about.html")

def contact(request):

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            data = form.save()

            # Send email
            send_mail(
                subject="Thank you for visiting",
                message="Thank you for contacting me. I will reach you soon.",
                from_email=None,
                recipient_list=[data.email],
            )

            return render(request,"core/contact.html",{
                "form": ContactForm(),
                "success": True
            })

    return render(request,"core/contact.html", {"form": form})
