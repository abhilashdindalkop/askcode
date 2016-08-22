from rest_framework import serializers

from stack.models import UserAccounts

class StackSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserAccounts
		fields = ('username', 'password', 'name', 'email_id', 'address')



		