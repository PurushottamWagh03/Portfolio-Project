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

def skills(request):
    skills = {
        "languages": ["Python", "Java", "Kotlin"],
        "frameworks": ["Django", "HTML", "CSS", "XML"],
        "tools": ["Machine Learning", "NLP", "REST APIs", "Pandas", "scikit-learn", "NLTK"],
        "soft": ["Communication", "Leadership", "Problem Solving", "Critical Thinking"]
    }
    return render(request, "core/skills.html", {"skills": skills})

def achievements(request):
    achievements = [
        "Java Programming Intermediate – Cipher School (July 2025)",
        "ChatGPT-4 Prompt Engineering Certification (June 2025)",
        "Privacy and Security on Social Media – NPTEL",
        "Volunteer Certification – Stambh Organization",
        "IT Voice Expo Technical Fest Participation (Jaipur)"
    ]
    return render(request, "core/achievements.html", {"achievements": achievements})