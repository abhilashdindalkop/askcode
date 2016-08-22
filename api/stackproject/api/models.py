from django.db import models

# Create your models here.
from stack.models import UserAccounts, Session

def getAllUsers():
	return UserAccounts.objects.all()


def get_object(username):
	try:
		return UserAccounts.objects.get(username = username)
	except UserAccounts.DoesNotExist:
	    raise Http404

def create_session(userid):
    user = UserAccounts.objects.get(id = userid)
    usersession = Session(user_id = user)
    usersession.save()
    return usersession.session_id