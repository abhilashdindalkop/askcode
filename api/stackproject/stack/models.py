from django.db import models
import uuid
# Create your models here.

class UserAccounts(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=70, blank=True, null=True, unique=True)
    address = models.CharField(max_length=200)


class Session(models.Model):
	user_id = models.ForeignKey(UserAccounts)
	session_id = models.UUIDField(unique=True, default=uuid.uuid4)

class Questions(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	user_id = models.ForeignKey(UserAccounts)
	valid_ans = models.IntegerField(null=True, blank=True)

class Answers(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	question_id = models.ForeignKey(Questions)
	owner_id = models.ForeignKey(UserAccounts)

class Tags(models.Model):
	name = models.CharField(unique=True, max_length=200)

class QuestionTags(models.Model):
	question_id = models.ForeignKey(Questions)
	tag_id = models.ForeignKey(Tags)


class AnswerVote(models.Model):
	voter_id = models.ForeignKey(UserAccounts)
	answer_id = models.ForeignKey(Answers)
	vote_type = models.IntegerField()