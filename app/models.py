from django.db import models
from django.conf import settings



User = settings.AUTH_USER_MODEL
class ToDo(models.Model):
	user  =  models.ForeignKey(User,default=1,on_delete=models.CASCADE)
	task = models.CharField(max_length=30)
	completed = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-updated']

	def __str__(self):
		return self.task

	


