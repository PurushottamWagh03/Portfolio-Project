from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from projects.models import Project

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    for project in projects:
        project.tech_list = project.tech_stack.split(',')
        
    skills_data = {
        "languages": [
            {"name": "Python", "classes": "bg-blue-500/10 text-blue-400 border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.15)]"},
            {"name": "Java", "classes": "bg-orange-500/10 text-orange-400 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.15)]"},
            {"name": "Kotlin", "classes": "bg-purple-500/10 text-purple-400 border-purple-500/30 shadow-[0_0_15px_rgba(168,85,247,0.15)]"}
        ],
        "frameworks": [
            {"name": "Django", "classes": "bg-emerald-500/10 text-emerald-400 border-emerald-500/30 shadow-[0_0_15px_rgba(16,185,129,0.15)]"},
            {"name": "HTML", "classes": "bg-orange-500/10 text-orange-400 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.15)]"},
            {"name": "CSS", "classes": "bg-blue-500/10 text-blue-400 border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.15)]"},
            {"name": "XML", "classes": "bg-yellow-500/10 text-yellow-500 border-yellow-500/30 shadow-[0_0_15px_rgba(234,179,8,0.15)]"}
        ],
        "tools": [
            {"name": "Machine Learning", "classes": "bg-pink-500/10 text-pink-400 border-pink-500/30 shadow-[0_0_15px_rgba(236,72,153,0.15)]"},
            {"name": "NLP", "classes": "bg-cyan-500/10 text-cyan-400 border-cyan-500/30 shadow-[0_0_15px_rgba(6,182,212,0.15)]"},
            {"name": "REST APIs", "classes": "bg-green-500/10 text-green-400 border-green-500/30 shadow-[0_0_15px_rgba(34,197,94,0.15)]"},
            {"name": "Pandas", "classes": "bg-blue-500/10 text-blue-400 border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.15)]"},
            {"name": "scikit-learn", "classes": "bg-orange-500/10 text-orange-400 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.15)]"},
            {"name": "NLTK", "classes": "bg-yellow-500/10 text-yellow-500 border-yellow-500/30 shadow-[0_0_15px_rgba(234,179,8,0.15)]"}
        ],
        "soft": [
            {"name": "Communication", "classes": "bg-brand-cyan/20 text-brand-cyan border-brand-cyan/30 shadow-[0_0_15px_rgba(6,182,212,0.2)]"},
            {"name": "Leadership", "classes": "bg-brand-indigo/20 text-brand-indigo border-brand-indigo/30 shadow-[0_0_15px_rgba(99,102,241,0.2)]"},
            {"name": "Problem Solving", "classes": "bg-brand-purple/20 text-brand-purple border-brand-purple/30 shadow-[0_0_15px_rgba(168,85,247,0.2)]"},
            {"name": "Critical Thinking", "classes": "bg-pink-500/20 text-pink-400 border-pink-500/30 shadow-[0_0_15px_rgba(236,72,153,0.2)]"}
        ]
    }
    
    achievements_data = [
        "Real world project and educational task completion with top educator as freelancer",
        "Volunteer Certification – Stambh Organization",
        "IT Voice Expo Technical Fest Participation (Jaipur)"
    ]
    
    certs = [
        {"title": "Master Generative AI & Generative AI tools (ChatGPT & more)", "issuer": "Udemy", "date": "Aug 31, 2025", "instructor": "Saad A", "duration": "14 total hours", "image": "cert_udemy_gen_ai.png"},
        {"title": "Build Generative AI Apps and Solutions with No-Code Tools", "issuer": "Udemy", "date": "Aug 26, 2025", "instructor": "Henry Habib", "duration": "5.5 total hours", "image": "cert_udemy_nocode.png"},
        {"title": "Privacy and Security in Online Social Media", "issuer": "NPTEL", "date": "Jan-Apr 2025", "instructor": "Prof. Kishore Kothapalli & Prof. Andrew Thangaraj", "duration": "12 week course (53%)", "image": "cert_nptel.png"},
        {"title": "Java with OOPs - Programming Language", "issuer": "CipherSchools", "date": "June 4, 2025 to July 15, 2025", "instructor": "Anurag Mishra", "duration": "70 hours", "image": "cert_cipher.png"}
    ]
    
    form = ContactForm()
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_mail(
                subject="Thank you for visiting",
                message="Thank you for contacting me. I will reach you soon.",
                from_email=None,
                recipient_list=[data.email],
            )
            form = ContactForm()
            success = True
            # Optional: redirect back to home with success hash
            return redirect('/#contact-success')

    context = {
        "profile": profile,
        "projects": projects,
        "skills": skills_data,
        "achievements": achievements_data,
        "certificates": certs,
        "form": form,
        "success": success
    }
    return render(request, "core/home.html", context)

def about(request):
    return render(request, "core/about.html")

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save()
            send_mail(
                subject="Thank you for visiting",
                message="Thank you for contacting me. I will reach you soon.",
                from_email=None,
                recipient_list=[data.email],
            )
            return render(request,"core/contact.html",{"form": ContactForm(), "success": True})
    return render(request,"core/contact.html", {"form": form})

def skills(request):
    skills_data = {
        "languages": [
            {"name": "Python", "classes": "bg-blue-500/10 text-blue-400 border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.15)]"},
            {"name": "Java", "classes": "bg-orange-500/10 text-orange-400 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.15)]"},
            {"name": "Kotlin", "classes": "bg-purple-500/10 text-purple-400 border-purple-500/30 shadow-[0_0_15px_rgba(168,85,247,0.15)]"}
        ],
        "frameworks": [
            {"name": "Django", "classes": "bg-emerald-500/10 text-emerald-400 border-emerald-500/30 shadow-[0_0_15px_rgba(16,185,129,0.15)]"},
            {"name": "HTML", "classes": "bg-orange-500/10 text-orange-400 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.15)]"},
            {"name": "CSS", "classes": "bg-blue-500/10 text-blue-400 border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.15)]"},
            {"name": "XML", "classes": "bg-yellow-500/10 text-yellow-500 border-yellow-500/30 shadow-[0_0_15px_rgba(234,179,8,0.15)]"}
        ],
        "tools": [
            {"name": "Machine Learning", "classes": "bg-pink-500/10 text-pink-400 border-pink-500/30 shadow-[0_0_15px_rgba(236,72,153,0.15)]"},
            {"name": "NLP", "classes": "bg-cyan-500/10 text-cyan-400 border-cyan-500/30 shadow-[0_0_15px_rgba(6,182,212,0.15)]"},
            {"name": "REST APIs", "classes": "bg-green-500/10 text-green-400 border-green-500/30 shadow-[0_0_15px_rgba(34,197,94,0.15)]"},
            {"name": "Pandas", "classes": "bg-blue-500/10 text-blue-400 border-blue-500/30 shadow-[0_0_15px_rgba(59,130,246,0.15)]"},
            {"name": "scikit-learn", "classes": "bg-orange-500/10 text-orange-400 border-orange-500/30 shadow-[0_0_15px_rgba(249,115,22,0.15)]"},
            {"name": "NLTK", "classes": "bg-yellow-500/10 text-yellow-500 border-yellow-500/30 shadow-[0_0_15px_rgba(234,179,8,0.15)]"}
        ],
        "soft": [
            {"name": "Communication", "classes": "bg-brand-cyan/20 text-brand-cyan border-brand-cyan/30 shadow-[0_0_15px_rgba(6,182,212,0.2)]"},
            {"name": "Leadership", "classes": "bg-brand-indigo/20 text-brand-indigo border-brand-indigo/30 shadow-[0_0_15px_rgba(99,102,241,0.2)]"},
            {"name": "Problem Solving", "classes": "bg-brand-purple/20 text-brand-purple border-brand-purple/30 shadow-[0_0_15px_rgba(168,85,247,0.2)]"},
            {"name": "Critical Thinking", "classes": "bg-pink-500/20 text-pink-400 border-pink-500/30 shadow-[0_0_15px_rgba(236,72,153,0.2)]"}
        ]
    }
    return render(request, "core/skills.html", {"skills": skills_data})

def achievements(request):
    achievements_data = [
        "Real world project and educational task completion with top educator as freelancer",
        "Volunteer Certification – Stambh Organization",
        "IT Voice Expo Technical Fest Participation (Jaipur)"
    ]
    return render(request, "core/achievements.html", {"achievements": achievements_data})

def certificates(request):
    certs = [
        {"title": "Master Generative AI & Generative AI tools (ChatGPT & more)", "issuer": "Udemy", "date": "Aug 31, 2025", "instructor": "Saad A", "duration": "14 total hours", "image": "cert_udemy_gen_ai.png"},
        {"title": "Build Generative AI Apps and Solutions with No-Code Tools", "issuer": "Udemy", "date": "Aug 26, 2025", "instructor": "Henry Habib", "duration": "5.5 total hours", "image": "cert_udemy_nocode.png"},
        {"title": "Privacy and Security in Online Social Media", "issuer": "NPTEL", "date": "Jan-Apr 2025", "instructor": "Prof. Kishore Kothapalli & Prof. Andrew Thangaraj", "duration": "12 week course (53%)", "image": "cert_nptel.png"},
        {"title": "Java with OOPs - Programming Language", "issuer": "CipherSchools", "date": "June 4, 2025 to July 15, 2025", "instructor": "Anurag Mishra", "duration": "70 hours", "image": "cert_cipher.png"}
    ]
    return render(request, "core/certificates.html", {"certificates": certs})

def magic_load_data(request):
    import sys
    from io import StringIO
    from django.core.management import call_command
    from django.http import HttpResponse
    
    out = StringIO()
    try:
        call_command('loaddata', 'datadump.json', stdout=out, stderr=out)
        return HttpResponse(f"<h1>SUCCESS</h1><pre>{out.getvalue()}</pre>")
    except Exception as e:
        return HttpResponse(f"<h1>ERROR</h1><p>{str(e)}</p><pre>{out.getvalue()}</pre>")