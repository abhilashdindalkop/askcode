from django.db import models

# Create your models here.
from stack.models import UserAccounts, Session, Questions, Answers, Tags, QuestionTags, AnswerVote

def getAllQuestions(uid):
	return Questions.objects.filter(user_id = uid)


# handle exception if session not found
def getCurrentUser(session_id):
	return Session.objects.get(session_id = session_id).user_id


# handle exception if question not found
def getAllAnswers(qid):
	return Answers.objects.filter(question_id = qid)

def getTagid(tagname):
	return Tags.objects.get(name = tagname)

def getQuestionId(qid):
	return Questions.objects.get(id = qid)

def add_tag_to_question(qid, tagid):
	QuestionTags(question_id=qid, tag_id=tagid).save()

def get_Tag_Names(qid):
	tagnames = list()
	mytags = QuestionTags.objects.filter(question_id=qid)
	for tag in mytags:
		tagnames.append(tag.tag_id.name)
	return tagnames

def search_questions(search_txt):
	resque = Questions.objects.filter(title__icontains=search_txt)
	return resque


def vote_answer(ansid, voterid, votetype):

	ans = Answers.objects.get(id = ansid)

	AnswerVote(voter_id = voterid, answer_id = ans, vote_type=votetype).save()

def getTotalVotes(ansid):
	ans = Answers.objects.get(id = ansid)
	votes = AnswerVote.objects.filter(answer_id = ans)
	total = 0
	for vote in votes:
		total = (total) + (vote.vote_type)
	return total