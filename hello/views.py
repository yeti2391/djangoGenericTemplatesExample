from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View 
import textwrap
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(View):
    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
        <html>
        <head>
            <title>Greetings to the world</title>
        </head>
        <body>
            <h1>To the world!</h1>
            <p>Hello, World!</p>
        </body>
        </html>
        ''')
        return HttpResponse(response_text)

class CourseView(TemplateView):
    template_name = "course.html"