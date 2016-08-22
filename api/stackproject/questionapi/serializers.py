from rest_framework import serializers

from stack.models import Questions, Answers

class QuestionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Questions
		fields = ('id', 'title', 'description', 'user_id', 'valid_ans')

class AnswerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Answers
		fields = ('id', 'title', 'description', 'question_id', 'owner_id')