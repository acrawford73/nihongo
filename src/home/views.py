from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.
class Index(TemplateView):
	template_name = 'home/index.html'

class Hiragana(TemplateView):
	template_name = 'home/hiragana.html'

class Katakana(TemplateView):
	template_name = 'home/katakana.html'

class Resources(TemplateView):
	template_name = 'home/resources.html'

class Help(TemplateView):
	template_name = 'home/help.html'

class Social(TemplateView):
	template_name = 'home/social.html'

class Donate(TemplateView):
	template_name = 'home/donate.html'

class About(TemplateView):
	template_name = 'home/about.html'

class Terms(TemplateView):
	template_name = 'home/terms.html'

class Privacy(TemplateView):
	template_name = 'home/privacy.html'


