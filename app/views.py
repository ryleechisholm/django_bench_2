from django.shortcuts import render
from django.http import HttpRequest
from app.info import SUBJECTS

def home_page(request: HttpRequest):
    return render(request, "home.html")

def subject_page(request: HttpRequest, subject: str):
    for num in SUBJECTS:
        if subject == num.key_title:
            return render(request, "subj_temp.html", {"title": num.title, "info": num.info, "specs": num.specs})
