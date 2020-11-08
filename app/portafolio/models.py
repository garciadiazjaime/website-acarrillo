from django.db import models
from django.forms import ModelForm
from django import forms
from tinymce.models import HTMLField

class Project(models.Model):
	title = models.CharField(max_length=140)
	slug = models.CharField(max_length=140)
	description = HTMLField()
	extra = models.CharField(max_length=1000, blank=True, null=True)
	status = models.BooleanField(default=True)
	weight = models.IntegerField(default=0)
	date_created = models.DateField(auto_now=True)

	def __unicode__(self):
		return u'%s' %  (self.title)

class ProjectForm(ModelForm):

	class Meta:
		model = Project
		exclude = ['date_created', 'weight', 'status']
		widgets = {
			'description': forms.Textarea(attrs={'rows':4, 'cols':5}),
			'extra': forms.Textarea(attrs={'rows':4, 'cols':5}),
		}

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class' : 'form-control'})
		self.fields['slug'].widget.attrs.update({'class' : 'form-control'})
		self.fields['description'].widget.attrs.update({'class' : 'form-control'})
		self.fields['extra'].widget.attrs.update({'class' : 'form-control'})


class Item(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	title = models.CharField(max_length=250, blank=True, null=True)
	image = models.ImageField(upload_to='portafolio/images', blank=True, null=True)
	weight = models.IntegerField(default=0)

	def __unicode__(self):
		return u'%s' %  (self.image.name)

class ItemForm(ModelForm):

	class Meta:
		model = Item
		fields = ['image', 'title']
		exclude = ['project', 'weight', 'id']

	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		self.fields['image'].widget.attrs.update({'class' : 'form-control'})
		self.fields['title'].widget.attrs.update({'class' : 'form-control', 'placeholder':'image title'})
