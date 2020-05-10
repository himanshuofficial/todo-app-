from django import forms
from django.forms import ModelForm
from .models import ToDo



class TaskForm(ModelForm):


	class Meta:
		model = ToDo
		fields = ['task']

class UpdateForm(ModelForm):
	class Meta:
		model = ToDo
		fields = ['task','completed']