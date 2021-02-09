from django.db import models
from django.db import connection 
from django.contrib.auth.models import User

# Create your models here.
class QuestionManager(models.Manager):
	def new(self):
		connection.cursor.execute("SELECT * FROM qa_question qa ORDER BY qa.added_at DESC")
		result_list = []
		for row in connection.cursor.fetchall():
			result_list.append(row)
		return result_list
	
	def popular(self):
		connection.cursor.execute("SELECT * FROM qa_question qa ORDER BY qa.rating DESC")
		result_list = []
		for row in connection.cursor.fetchall():
			result_list.append(row)
		return result_list

class Question(models.Model):
	title = models.CharField(max_length=191)
	text = models.TextField()
	added_at = models.DateTimeField()
	rating = models.IntegerField()
	author = models.CharField(max_length=191)
	likes = models.TextField()

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField()
	question = models.CharField(max_length=191)
	author = models.CharField(max_length=191)

class Person(User):
	objects = models.Manager()
